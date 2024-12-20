from fnmatch import *

for n in range(2025, 10**10, 2025):
	if fnmatch(str(n), '33?2*42?') and fnmatch(str(n), '*32??2?'):
		print(n, n // 2025)