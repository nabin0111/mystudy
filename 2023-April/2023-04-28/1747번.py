def isPrime(n):
    if n == 1:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** (1/2)) + 1, 2):
        if n % i == 0:
            return False
    return True

N = int(input())
while True:
    if str(N) == str(N)[::-1]:
        if isPrime(N):
            print(N)
            break
    N += 1