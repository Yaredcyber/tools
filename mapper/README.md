# Mapper
![image](https://github.com/Yaredcyber/tools/assets/147349965/e4469032-47ab-4a20-aba6-8165f14c162b)


- **Is Simple Port scanner for remote machine and also local computer**
- **It is used to information gathering tool**
- **It is written in python language**
## Features of Mapper ⚙
> - <h3 style="font-style:italic;"> Scan Port
> - <h3 style="font-style:italic;"> Scan Services
## Installation  ⬇
```bash
git clone https://github.com/Yaredcyber/tools.git
```
```bash
sudo mv tools/mapper . && rm -rf tools && cd mapper
```
## Example
```
python3 mapper.py -i 127.0.0.1 -s 1 -e 22 -t 1
```
>- #-i = IP adress of the host
>- #-s = Start port by defult it is 1
>- #-e = End port by defult it is 1000
>- *-t = time out it is also 0.5 sec
>- #-b = Browse resources it take one argument g 


<hr>

- *The new incomming  version of mapper will  able to scan system os and service version*
