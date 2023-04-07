N, K = map(int, input().split())
u, d = 1, 1

for i in range(K):
    u *= (N-i)
    d *= (K-i)

print(u // d)