#!/usr/bin/env python3
# Script to f3tch t3h fl4gz0rx

import base64
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

from pwn import *
import gmpy2

AES_BLOCK_SIZE = 32
AES_KEY_SIZE = 32

B = 12345678910
HOST = 'isc2023.1337.cx'
PORT = 11048

def get_aes_key(shared_num, salt):
    bnum = shared_num.to_bytes((shared_num.bit_length() + 7) // 8, byteorder='big')
    return scrypt(bnum, salt, AES_BLOCK_SIZE, N=2**14, r=8, p=1)

def decrypt_aes(msg, key):
    # pass # TODO you should be able to easily figure out the mode
    aes = AES.new(key, AES.MODE_ECB)
    dec = aes.decrypt(msg)
    return dec

def remove_beginning_and_end(input_string, beginning_substring, end_substring):
    
    # Remove the beginning substring
    input_string = input_string.lstrip(beginning_substring)
    
    # Remove the end substring
    input_string = input_string.replace(end_substring, "").strip()
    
    dec_str = base64.b64decode(input_string)
    return json.loads(dec_str)

if __name__ == "__main__":
    
    conn = remote(HOST, PORT)

    # Receive data from the server
    data = conn.recv().decode("utf-8")
    
    # decode base 64
    resp_1 = remove_beginning_and_end(data, 'BEGIN_HANDSHAKE\n', 'INPUT_YOUR_NUMBER:')
    # print("1st msg: ", resp_1)
    
    # data for DH
    g = resp_1["g"]
    A = resp_1["A"]
    p = resp_1["p"]

    # compute gbp for DH
    gbp = gmpy2.powmod(g, B, p)
    shared_key = gmpy2.powmod(A, B, p)

    # Send B = g^b mod p to the server
    conn.sendline(str(gbp).encode())  # encode string to bytes and send to the server
    
    # Receive data from the server
    data = conn.recv().decode()
    
    resp_2 = remove_beginning_and_end(data, 'OKAY! BEGIN_MESSAGE', 'Connection closed by foreign host.')
    # print("2nd msg:", resp_2)
    
    # extract decoded msg and salt
    msg = base64.b64decode(resp_2["msg"])
    salt = base64.b64decode(resp_2["salt"])
    
    aes_key = get_aes_key(int (shared_key), salt)
    dec = decrypt_aes(msg, aes_key)
    
    pattern = r'SpeishFlag\{.*?\}'
    matches = re.findall(pattern, dec.decode())
    print(matches[0])
    
    with open('../sol/flag1', 'w') as f:
        f.write(matches[0])