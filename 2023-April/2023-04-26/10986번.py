import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num = [i % M for i in num]
c = [0] * (M)
p = [0] * (N+1)
for i in range(N):
    p[i+1] = (p[i] + num[i]) % M
    c[p[i+1]] += 1
result = c[0]
for i in range(M):
    result += c[i] * (c[i] - 1) // 2
print(result)