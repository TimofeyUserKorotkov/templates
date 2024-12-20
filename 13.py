from ipaddress import *

net = ip_network(f'222.121.128.0/255.255.224.0')
cnt = 0
for ip in net:
	b = bin(int(ip))[2:].zfill(32)
	if b[-1] == b[-2]:
		cnt += 1
print(cnt)