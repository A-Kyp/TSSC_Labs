# Lab 8 - Network Security

**Infrastructura:** Trebuie facut pe OpenStack si ultimul exercitiu pe Docker


## Task 1
### A
```bash
nmap -sn 10.9.1-4.0-255
```

### B
```bash
sudo nmap -sS -sU -sV -T4 -p 10002 10.9.1.113
```

### C
```bash
sudo nmap -O 10.9.2.100
```

## Task 2

### A - Intro
```bash
sudo iptables -I INPUT -s 141.85.241.63 -j ACCEPT
```

### B 
```bash
ssh hacker@10.9.2.100
(hacker) wall "Wazzaap?"
(hacker) exit

tcpdump -i eth0 'host not 141.85.241.63'

```

### D
```bash
sudo iptables -A OUTPUT -m string --algo bm --string "facebook" -j DROP
```

## Task 3

### A

```bash
# turn on IP Forwarding -- for the attacker (inherited from host)
# containers don't have permission for this and we don't want to bother with capabilities
sudo sysctl -w net.ipv4.ip_forward=1
 
# Open a "Victim" terminal (on your VM):
docker run --rm -ti --entrypoint /bin/bash --name victim ubuntu:22.04
# Open an "Attacker" terminal (also on the same VM):
docker run --rm -ti --entrypoint /bin/bash --name attacker --sysctl net.ipv4.ip_forward=1 ubuntu:22.04
 
# we need two terminals for the attacker (for the tcpdump later)
# so... in a third terminal, spawn a Docker exec shell:
docker exec -ti attacker /bin/bash
```
Victim terminal
```bash
apt update && apt install -y iproute2 iputils-ping netcat-openbsd
ip a sh
```
Attacker terminal
```bash
# install prerequisites for this task
apt update && apt install -y dsniff tcpdump iproute2 iputils-ping
 
# start poisoning the host's ARP cache
#arpspoof -i <INTERFACE> -t <VICTIM_IP> <GATEWAY_IP> -r
arpspoof -i eth0 -t 172.17.0.2 172.17.0.1 -r
```

### B
Attacker terminal (celalalt)
```bash
tcpdump udp port 53 -nvvX
```
Victim terminal
```bash
# check ARP table (your gateway's MAC should be the attacker's)
ip nei sh
# ping your favorite website
ping my.secretwebsite.com
# Unfortunately, IP forwarding inside container doesn't work :(
```
