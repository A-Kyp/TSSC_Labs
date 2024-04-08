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
```bash
gcc buggy.c -o buggy -fno-stack-protector -m32 -g
```

## Task 2
```bash
# Run the program using GDB, setting the argument Florin.
gdb buggy
# Set a breakpoint at the beginning of the main function.
# Continue execution until you hit the breakpoint.
break main
run Florin

#alternativ, se poate folosi start 
start


# Try to reach the beginning of the copy function without setting another breakpoint.
n #de 3 ori

```

## Task 3

```bash
# Remove the existing breakpoint and set a new one at the beginning of the copy function.
i b
d 1
i b
b copy
# Run again the program and continue execution until you hit the breakpoint.
run Florin
# Print the value and the address of name. Print the value again after gets(name) is executed.
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

show disable-randomization
set disable-randomization off
```

## Task 5