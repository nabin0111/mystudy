from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
ans = []
for i in range(n):
    cur = list(map(int, input().split()))
    maps.append(cur)
    ans.append(cur)
    if 2 in cur:
        j = cur.index(2)
        target = (i, j)
        ans[i][j] = 0

q = deque([target])
no = set()
while q:
    r, c = q.popleft()
    pre = ans[r][c] + 1

    for a, b in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if 0 <= a < n and 0 <= b < m and maps[a][b] == 1:
            if (a, b) == target or (a, b) in no:
                continue
            now = ans[a][b]
            if pre == 1:
                no.add((a, b))
            if now == 1 or now > pre:
                ans[a][b] = pre
                q.append((a, b))
for i in range(n):
    for j in range(m):
        if ans[i][j] == 1 and (i, j) not in no:
            ans[i][j] = -1
for i in ans:
    print(*i)