de pe vm openstack
```bash
chown red:red -R /home/red/.ssh
```
de pe fep 
```bash
ssh -i ~/.ssh/openstack.key red@10.9.1.217
```

din green/red/blue
```bash
gpg --full-generate-key
gpg --export --armor green@cs.pub.ro green_key.txt > green_key.txt
cp green_key.txt /tmp/
gpg --import /tmp/red_key.txt

gpg -o secret_file.txt.gpg -e -r red@cs.pub.ro secret_file.txt
```

din red
```bash
gpg --decrypt /tmp/secret_file.txt.gpg
```

din green
```bash
gpg --output /tmp/green/signed-red.gpg --sign /tmp/red_key.txt

```

```bash
gpg --export --armor red@cs.pub.ro > /tmp/red_signed.txt
gpg --signe-key red@cs.pub.ro
```

pt tor
```bash
ssh -J fep -L 9050:localhost:9050 openstack
```
