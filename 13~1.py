from ipaddress import *

net = ip_network('172.16.80.0/255.255.248.0')
print(sum(f'{i:b}'.count('1') % 2 for i in net))
