
#13 максимальное а суммарное колво единиц в левых двух байтах не менее суммарного колва удиниц в правых двух байтах
from ipaddress import *
for a in range(255+1):
    ip_net = ip_network(f"127.254.{a}.10/255.255.224.0", False)
    for ip_ad in ip_net:
        if (bin(int(ip_ad))[-16:].count("1") <= bin(int(ip_ad))[:-16].count("1")) == False:
            break

    else:
        print(a)
