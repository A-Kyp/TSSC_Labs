def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext

ciphertext = "wAyk{mmAwjAuwpz AwmAqjn"

# Iterate over all possible keys
for i in range(256):
    key = chr(i) * len(ciphertext)
    decrypted_text = decrypt(ciphertext, key)
    
    if decrypted_text.isprintable():
        print(decrypted_text)
