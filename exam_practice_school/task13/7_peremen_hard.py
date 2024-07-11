#13 peremennaya
from ipaddress import *
for A in range(0,256):
    ip_net = ip_network(f"127.254.{A}.19/255.255.224.0", False)
    for ip_ad in ip_net:
        if bin(int(ip_ad))[-16:].count("1") > bin(int(ip_ad))[:-16].count("1") == False:
            break
        else:
            print(A)