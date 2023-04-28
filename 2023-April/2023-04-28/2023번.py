N = int(input())

def isPrime(n):
    if n == 1:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for i in range(3, int(n ** (1/2)) + 1, 2):
        if n % i == 0:
            return False
    return True

p = [2, 3, 5, 7]
for i in p:
    if len(str(i)) == N:
        print(i)
        continue
    for j in range(1, 10):
        tmp = int(str(i)+str(j))
        if isPrime(tmp):
            p.append(tmp)
