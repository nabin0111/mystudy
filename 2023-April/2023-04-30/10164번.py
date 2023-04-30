N, M, K = map(int, input().split())
tx, ty = (K-1)%M, (K-1)//M
if K == 0:
    tx, ty = -1, -1
table = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if j < tx and i > ty:
            continue
        elif j > tx and i < ty:
            continue
        elif i == 0 or j == 0:
            table[i][j] = 1
            continue
        u = table[i-1][j]
        l = table[i][j-1]
        table[i][j] = u + l
print(table[N-1][M-1])