from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(input().rstrip())

q = deque()
q.append((0, 0, 1))
visit = [[False] * M for _ in range(N)]
visit[0][0] = True

while q:
    r, c, cnt = q.popleft()

    if r == N-1 and c == M-1:
        print(cnt)
        break

    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == '1' and not visit[nr][nc]:
            q.append((nr, nc, cnt+1))
            visit[nr][nc] = True