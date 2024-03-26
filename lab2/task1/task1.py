from Crypto.Cipher import AES
from Crypto import Random
 
BLOCK_SIZE = 32
PADDING = b'#'
iv = b"\x00" * 16
 
# def encrypt(key, iv, data):
#     aes = AES.new(key, AES.MODE_CBC, iv)
#     data = aes.encrypt(data)
#     return data
 
# def pad(s):
#     return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING 
 
def decrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = aes.decrypt(data)
    return data
 
with open('isc-lab02-secret.enc', 'rb') as f:
    enc_data = f.read()
    
key = enc_data[:BLOCK_SIZE]
cipher = enc_data[BLOCK_SIZE:]
dec_data = decrypt(key, iv, cipher).rstrip(PADDING)
 
with open('isc-lab02-secret.jpg', 'wb') as out:
    out.write(dec_data)