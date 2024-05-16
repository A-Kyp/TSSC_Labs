#!/usr/bin/env python3
# Script to f3tch t3h fl4gz0rx

import os
import base64
import json
from Crypto.Cipher import AES
from Crypto.Util import number
from Crypto.Protocol.KDF import scrypt

import socket
import gmpy2
from Crypto.Util.Padding import unpad, pad

AES_BLOCK_SIZE = 32
AES_KEY_SIZE = 32

B = 12345678910

def get_aes_key(shared_num, salt):
    bnum = shared_num.to_bytes((shared_num.bit_length() + 7) // 8, byteorder='big')
    return scrypt(bnum, salt, AES_BLOCK_SIZE, N=2**14, r=8, p=1)

def decrypt_aes(msg, key):
    # pass # TODO you should be able to easily figure out the mode
    aes = AES.new(key, AES.MODE_ECB)
    data = aes.decrypt(msg)
    return data

def is_utf8(byte_array):
    try:
        byte_array.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

def remove_beginning_and_end(input_string, beginning_substring, end_substring):
    # Remove the beginning substring
    input_string = input_string.lstrip(beginning_substring)
    
    # Remove the end substring
    input_string = input_string.rstrip(end_substring)
    
    dec_str = base64.b64decode(input_string)
    
    return json.loads(message)


def get_dict(data, begin=True):
    if not isinstance(data, str):
        decoded_data = data.decode()
    else:
        decoded_data = data

    if begin:
        extracted_data = (
            (decoded_data.split("BEGIN_HANDSHAKE"))[1]
            .split("INPUT_YOUR_NUMBER: ")[0]
            .replace("\n", "")
        )
    else:
        extracted_data = (
            (decoded_data.split("OKAY! BEGIN_MESSAGE"))[1]
            .split("Connection closed by foreign host.")[0]
            .replace("\n", "")
        )
    message = base64.b64decode(extracted_data)
    return json.loads(message)

if __name__ == "__main__":
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port to which you want to connect
    host = 'isc2023.1337.cx'
    port = 11048

    # Connect to the server
    client_socket.connect((host, port))

    # Receive data from the server
    data = client_socket.recv(1024).decode()  # receive up to 1024 bytes and decode from bytes to string
    
    # decode base 64
    resp_1 = get_dict(data, begin=True)
    print("1st msg: ", resp_1)
    
    # data for DH
    g = resp_1["g"]
    A = resp_1["A"]
    p = resp_1["p"]

    # compute gbp for DH
    gbp = gmpy2.powmod(g, B, p)
    shared_key = gmpy2.powmod(A, B, p)

    # Send data to the server
    message = str(gbp) + "\n"
    
    client_socket.send(message.encode())  # encode string to bytes and send to the server
    
    # Receive data from the server
    data = client_socket.recv(1024).decode()  # receive up to 1024 bytes and decode from bytes to string
    enc_data_2 = get_dict(data, begin=False)
    
    print("2nd msg:", enc_data_2)
    
    # extract decoded msg and salt
    msg = base64.b64decode(enc_data_2["msg"])
    salt = base64.b64decode(enc_data_2["salt"])
    
    aes_key = get_aes_key(int (shared_key), salt)
    
    dec = decrypt_aes(msg, aes_key)
    print("aes-decrypted-msg", dec.decode())
    
    # Close the connection
    client_socket.close()

