import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

N = int(input())
num = sorted([int(input()) for _ in range(N)])
M = []
g = num[1] - num[0]
for i in range(2, N):
    g = gcd(g, num[i]-num[i-1])
for i in range(2, int(g ** (1/2))+1):
    if g % i == 0:
        M.append(i)
        if g // i != i:
            M.append(g//i)
print(*sorted(M), g)