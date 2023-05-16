from itertools import combinations
from collections import deque

stu = ''
for _ in range(5):
    stu += input()

def bfs(loc):
    table = [[0]*5 for _ in range(5)]
    for r, c in loc:
        table[r][c] = 1
    q = deque([loc[0]])
    visit = [[0]*5 for _ in range(5)]
    visit[loc[0][0]][loc[0][1]] = 1
    while q:
        r, c = q.popleft()
        if table == visit:
            return True

        for a, b in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if 0 <= a < 5 and 0 <= b < 5 and table[a][b] == 1 and visit[a][b] == 0:
                visit[a][b] = 1
                q.append((a, b))
    return False

ans = 0
for c in combinations(range(25), 7):
    s = 0
    for n in c:
        if stu[n] == 'S':
            s += 1
    if s < 4:
        continue
    loc = [(i//5, i%5) for i in c]
    if bfs(loc):
        ans += 1
print(ans)