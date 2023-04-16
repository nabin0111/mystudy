import sys
input = sys.stdin.readline

def hur():
    r1, c1, r2, c2 = map(int, input().split())
    x, y, cur, cnt = 0, 0, 1, (r2-r1+1)*(c2-c1+1)
    S = [[1] * (c2-c1+1) for _ in range(r2-r1+1)]
    m, l = 1, 1
    d = [-1, 0]

    while cnt > 0:
        d[0] *= -1
        for j in range(2):
            for _ in range(l):
                if c1 <= x <= c2 and r1 <= y <= r2:
                    S[y-r1][x-c1] = cur
                    m = cur
                    cnt -= 1
                x += d[j]
                y -= d[1-j]
                cur += 1
        l += 1
    return S, m
S, m = hur()

for i in S:
    for j in i:
        print(f'{j:>{len(str(m))}}', end=' ')
    print()