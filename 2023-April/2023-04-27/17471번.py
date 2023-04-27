from itertools import combinations
from collections import deque

N = int(input())
pop = list(map(int, input().split()))
near = {}
for i in range(N):
    _, *con = map(int, input().split())
    near[i+1] = set(con)

def count(d_list):
    res = 0
    for d in d_list:
        res += pop[d-1]
    return res

def isConnected(d_list):
    q = deque()
    q.append(d_list[0])
    con = [0 for _ in range(N)]
    con[d_list[0]-1] = 1

    while q:
        cur = q.popleft()

        for i in near[cur]:
            if i in d_list and not con[i-1]:
                con[i-1] = 1
                q.append(i)
    
    return sum(con) == len(d_list)

dists = set(range(1, N+1))
ans = 1000
for i in range(1, N//2+1):
    d1s = tuple(combinations(dists, i))
    for d1 in d1s:
        d2 = list(dists.difference(d1))
        if isConnected(d1) and isConnected(d2):
            a = count(d1)
            b = count(d2)
            ans = min(ans, abs(a-b))
print(ans if ans != 1000 else -1)