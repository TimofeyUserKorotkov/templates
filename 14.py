from string import *

for x in reversed((digits + ascii_uppercase)[:25]):
	n = int(f'A4{x}7F2', 25) + int(f'N{x}G5{x}H', 25) + int(f'74{x}M26', 25)
	if n % 24 == 0:
		print(n // 24)
		break