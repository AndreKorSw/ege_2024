#13 количество единиц четно
from ipaddress import *
ip_nep = ip_network("192.168.32.160/255.255.255.240")
cnt = 0
for ip_ad in ip_nep:
    if bin(int(ip_ad))[2:].count("1") % 2 == 0:
        cnt+=1
print(cnt)