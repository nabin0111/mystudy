from collections import deque

N, L, R = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

def bfs(i, j):
    q = deque([(i, j)])
    union = [(i, j)]
    while q:
        r, c = q.popleft()
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+x, c+y
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                if L <= abs(maps[r][c] - maps[nr][nc]) <= R:
                    visit[nr][nc] = True
                    q.append((nr, nc))
                    union.append((nr, nc))
    return union

cnt = 0
while True:
    visit = [[False] * N for _ in range(N)]
    exist = False
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            visit[i][j] = True
            union = bfs(i, j)
            if len(union) > 1:
                exist = True
                tmp = sum([maps[r][c] for r, c in union]) // len(union)
                for r, c in union:
                    maps[r][c] = tmp
    if not exist:
        break
    cnt += 1
print(cnt)