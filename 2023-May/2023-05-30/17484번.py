from collections import deque
N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

q = deque([(0, i, maps[0][i], -2) for i in range(M)])
ans = float('inf')
while q:
    r, c, cnt, m = q.popleft()
    if r == N-1:
        ans = min(ans, cnt)
        continue

    for i in range(max(0, c-1), min(M, c+2)):
        if i == c-1 and m == -1:
            continue
        elif i == c and m == 0:
            continue
        elif i == c+1 and m == 1:
            continue
        q.append((r+1, i, cnt+maps[r+1][i], i-c))
print(ans)