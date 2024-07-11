#13 колво в правых больше левых
from ipaddress import *

ip_net = ip_network("", False)#false если дан конкретный адрес сети, а не общий
cnt = 0
for ip_ad in ip_net:
    if bin(int(ip_ad))[-16:].count("1") > bin(int(ip_ad))[:-16].count("1"):
        cnt +=1
print(cnt)