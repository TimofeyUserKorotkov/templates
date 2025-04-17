prime = lambda n: all(n % i for i in range(2, int(n**0.5) + 1)) and n > 1

def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return n > 1

print(prime(int(input())))

2147483647