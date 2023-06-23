import sys
input = sys.stdin.readline

N = int(input())
paint = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    paint.append(tmp)

for i in range(1, N):
    for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        paint[i][a] += min(paint[i-1][b], paint[i-1][c])

print(min(paint[N-1]))