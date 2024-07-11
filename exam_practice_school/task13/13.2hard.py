#13  минимальное значение а для которого колво единиц в левых двух байтах не менее суммарного колва единиц в правых двух байтах
from ipaddress import *
for i in range(9):# всего 8 возможных единиц
    a = i * "1" + 8 * "0"
    a = int(a[:8], 2)
    ip_net = ip_network(f"255.211.33.160/255.255.{a}.0", False)
    for ip_ad in ip_net:
        if (bin(int(ip_ad))[-16:].count("1") <=  bin(int(ip_ad))[:-16].count("1")) == False:
            break
    else:
        print(a)