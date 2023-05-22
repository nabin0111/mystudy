from itertools import combinations
N, M = map(int, input().split())
home, chick = [], []
for i in range(N):
    cur = input().split()
    home += [(i, j) for j, c in enumerate(cur) if c == '1']
    chick += [(i, j) for j, c in enumerate(cur) if c == '2']
ans = float('inf')
for comb in combinations(chick, M):
    m = [float('inf')] * len(home)
    for c in comb:
        for j, h in enumerate(home):
            m[j] = min(m[j], abs(c[0]-h[0]) + abs(c[1]-h[1]))
    ans = min(ans, sum(m))
print(ans)