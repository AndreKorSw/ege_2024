#минимальное а для которого суммарное колво единиц в левых двух байтах не менее суммарного колва единиц в правых двух байтах
from ipaddress import *

for i in range(9):
    a = i*"1" + 8 * "0"
    a = int(a[:8], 2)#берем только получившийся байт, отрезаем ненуженые нули и переводим все в десятинчную
    ip_net = ip_network(f"199.59.129.3/255.255.{a}.0", False)
    for ip_ad in ip_net:
        if (bin(int(ip_ad))[-16:].count("1") <=  bin(int(ip_ad))[:-16].count("1")) == False:
            break

    else:
        print(a)
