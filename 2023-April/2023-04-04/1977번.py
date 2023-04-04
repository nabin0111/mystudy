import sys
input = sys.stdin.readline

from math import sqrt, ceil, floor
M = int(input())
N = int(input())
m = ceil(sqrt(M))
n = floor(sqrt(N))
sum = 0

if m > n:
    print("-1")
else:
    for i in range(m, n+1):
        sum += i ** 2
    print(f'{sum}\n{m**2}')
