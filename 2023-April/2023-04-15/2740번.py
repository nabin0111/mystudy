N, M = map(int, input().split())
A, B = [], []
for i in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for i in range(M):
    B.append(list(map(int, input().split())))
C = []
for i in range(N):
    tmp = []
    for j in range(K):
        a = 0
        for k in range(M):
            a += A[i][k] * B[k][j]
        tmp.append(a)
    C.append(tmp)
for i in C:
    print(*i)