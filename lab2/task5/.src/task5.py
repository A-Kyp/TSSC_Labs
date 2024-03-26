import binascii

# Original and desired plaintexts
original_plaintext = "FIRE_NUKES_MELA!"
desired_plaintext = "SEND_NUDES_MELA!"

# Convert plaintexts to byte arrays
original_plaintext_bytes = original_plaintext.encode('utf-8')
desired_plaintext_bytes = desired_plaintext.encode('utf-8')

# Calculate the difference between original and desired plaintexts
difference = bytearray()
for i in range(len(original_plaintext_bytes)):
    difference.append(original_plaintext_bytes[i] ^ desired_plaintext_bytes[i])

# Original IV provided
original_iv_hex = "7ec00bc6fd663984c1b6c6fd95ceeef1"
original_iv_bytes = binascii.unhexlify(original_iv_hex)

# XOR the original IV with the difference to get the modified IV
modified_iv_bytes = bytearray()
for i in range(len(original_iv_bytes)):
    modified_iv_bytes.append(original_iv_bytes[i] ^ difference[i])

# Convert modified IV to hexadecimal string
modified_iv_hex = binascii.hexlify(modified_iv_bytes).decode('utf-8')

print("Modified IV (hex):", modified_iv_hex)
