import sys
input = sys.stdin.readline

def mul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            res = 0
            for i in range(n):
                res += A[r][i] * B[i][c]
            C[r][c] = res % 1000
    return C

def power(A, B):
    n = len(A)
    if B == 1:
        for r in range(n):
            for c in range(n):
                A[r][c] %= 1000
        return A
    elem = power(A, B//2)
    if B % 2 == 0:
        return mul(elem, elem)
    else:
        return mul(mul(elem, elem), A)

N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

X = power(A, B)
for i in X:
    print(*i)