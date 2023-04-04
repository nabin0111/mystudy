import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(1, K+1):
        if j < w:
            M[i][j] = M[i-1][j]
        else:
            M[i][j] = max(M[i-1][j], M[i-1][j-w] + v)
print(M[N][K])