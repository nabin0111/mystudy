import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K = K if K <= N-K else N-K
P = 1000000007

def calc(N, K):
    n, d = 1, 1
    for i in range(K, 0, -1):
        d = d * i % P
        n = n * N % P
        N -= 1
    return n, d

def power(n, p):
    if p == 0:
        return 1

    div = power(n, p//2)
    if p % 2 == 0:
        return div * div % P
    else:
        return div * div * n % P

n, d = calc(N, K)
d = power(d, P-2) % P
print(n * d % P)