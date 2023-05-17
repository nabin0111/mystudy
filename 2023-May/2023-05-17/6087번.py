from collections import deque
W, H = map(int, input().split())
s_map = []
cs = []
for i in range(H):
    tmp = list(input())
    cs += [(i, j) for j, c in enumerate(tmp) if c == 'C']
    s_map.append(tmp)

q = deque([cs[0]])
visited = [[10000]*W for _ in range(H)]
visited[cs[0][0]][cs[0][1]] = 0
while q:
    r, c = q.popleft()
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r+dr, c+dc
        while True:
            if 0 <= nr < H and 0 <= nc < W and s_map[nr][nc] != '*':
                if visited[nr][nc] > visited[r][c]:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c]+1
                else:
                    break
            else:
                break
            nr, nc = nr+dr, nc+dc
print(visited[cs[1][0]][cs[1][1]]-1)