from ipaddress import *
ip_net = ip_network("192.168.32.160/255.255.255.240")
c = 0
for ip_ad in ip_net:
    if bin(int(ip_ad))[2:].count("1") % 2 == 0:
        c += 1
print(c)



from ipaddress import *
ip_net = ip_network("192.128.32.160/255.255.255.240")
c = 0
for ip_ad in ip_net:
    if bin(int(ip_ad))[2:].count("1") > 8:
        c += 1
print(c)
