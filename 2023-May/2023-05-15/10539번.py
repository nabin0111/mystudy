N = int(input())
B = list(map(int, input().split()))
for i in range(N):
    B[i] = B[i] * (i+1)
for i in range(N-1, 0, -1):
    B[i] = B[i]-B[i-1]
print(*B)