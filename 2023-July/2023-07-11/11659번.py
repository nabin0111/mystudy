import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
p_sum = [0] * (N+1)
for i in range(N):
    p_sum[i+1] = p_sum[i] + num[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(p_sum[j] - p_sum[i-1])