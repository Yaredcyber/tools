##  Nmap scanning 
- nmap is known as a network mapper that used for scanning  and map network , IP address , host discovery , operating system and etc..

### live system discovery is checking up and down host (machine)
- -sn option used for  host discovery host up or down
```
nmap     "nmap -sn 192.168.56.1"
```
### scaning ports
- -Pn: used for scan  blocked  port from server
```
 nmap -Pn 192.168.56.1 
```
- -p- : Used for discover all 65,000 ports
```
nmap -p- 192.168.56.1
```
- -p port IP:  for scan specific port 
```
nmap -p 20 60 192.168.56.1
```
###  TCP scan 
-  it is work on 3 way hand shacke >>  St stand for "scan tcp"
```
 nmap -sT 192.168.56.1 
```
### Stealth scan 
-  same as TCP but not send Ack >> sS stand for "Stealth scan "
```
nmap -sS 192.168.56.1 
```
#### UDP scan
- it is one of transport protocols   sU >>stand for "scab UDP "
```
nmap -sU 192.168.56.1 

```
- All in one 
```
 nmap -sU -sS - -sX 192.168.56.1 
```
###  Xmas scan 
- it send FIN/PSH/URG instead of of SYN >> sX stand for "Xmas scan"
```
nmap -sX 192.168.56.1 
```
### scaninng speed 
### Nmap Agressive 
- it waits 1.25 sec 
```
nmap -T4 192.168.56.1
```
### Nmap Normal 
- dfault nmap timing 
```
 nmap -T3 192.168.56.1
##### Nmap Polite and sneaky
```
- slowest timing 
```
namp -T2 192.168.56.1
```

```
nmap -T1 192.168.56.1

```
###  nmap out put saving 
- -oG    >> Grampable format
- -oX    >> Xml format
-  -N    >> Normal saving 
### Nmap  out put detaile 
-  -V    >> litle detaile
-  -VV   >> detaile more
-  -VVV   >> much more detaile 
