de pe vm openstack
chown red:red -R /home/red/.ssh

de pe fep 
ssh -i ~/.ssh/openstack.key red@10.9.1.217

gpg --export --armor green@cs.pub.ro green_key.txt > green_key.txt
cp green_key.txt /tmp/

gpg --import /tmp/red_key.txt

