from ipaddress import *

ip_net = ip_network("255.67.33.87/255.252.0.0", False)
c = 0
for ip_ad in ip_net:
    if bin(int(ip_ad))[-16:].count("1") < 2 * bin(int(ip_ad))[:-16].count("1"):
        c+=1
print(bin(27))

