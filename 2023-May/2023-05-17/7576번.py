from collections import deque
W, H = map(int, input().split())
tomato = []
no = 0
for _ in range(H):
    tmp = list(map(int, input().split()))
    tomato.append(tmp)
    no += tmp.count(-1)

q = deque()
for i in range(H):
    for j in range(W):
        if tomato[i][j] == 1:
            q.append((i, j, 0))
cnt = 0
total = 0
while q:
    r, c, cnt = q.popleft()
    total += 1
    for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r+a, c+b
        if 0 <= nr < H and 0 <= nc < W and tomato[nr][nc] == 0:
            tomato[nr][nc] = 1
            q.append((nr, nc, cnt+1))
if total == W*H-no:
    print(cnt)
else:
    print(-1)