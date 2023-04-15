import sys
input = sys.stdin.readline

def check(a):
    c = int(a)
    return c**(1/2) % 1 == 0

def sqaure(table, N, M):
    result = -1

    for i in range(N):
        for j in range(M):
            for n in range(-N, N):
                for m in range(-M, M):
                    a = ""
                    x, y = i, j
                    if n == 0 and m == 0:
                        continue        
                    while x >= 0 and x < N and y >= 0 and y < M:
                        a += table[x][y]
                        x += n
                        y += m
                        if check(a):
                            result = max(result, int(a))       
    return result

N, M = map(int, input().split())
table = []
for _ in range(N):
    a = input().rstrip()
    table.append(list(a))
print(sqaure(table, N, M))
