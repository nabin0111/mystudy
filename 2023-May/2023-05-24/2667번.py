N = int(input())
maps = []
q = []
g = 0
for i in range(N):
    tmp = input()
    maps.append(tmp)
    for j, t in enumerate(tmp):
        if t == '1':
            q.append((i, j, g))
            g += 1
visited = [[False]*N for _ in range(N)]
ans = {}
while q:
    r, c, g = q.pop()
    if visited[r][c]:
        continue
    visited[r][c] = True
    if g in ans:
        ans[g] += 1
    else:
        ans[g] = 1

    for a, b in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
        if 0 <= a < N and 0 <= b < N and maps[a][b] == '1' and not visited[a][b]:
            q.append((a, b, g))
print(len(ans))
for i in sorted(ans.values()):
    print(i)