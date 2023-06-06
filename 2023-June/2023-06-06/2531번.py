from collections import defaultdict
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
rail = [int(input()) for _ in range(N)]
rail = rail+rail
l, r = 0, k-1
ans = 0

eat = defaultdict(int)
eat[c] += 1

for i in range(r+1):
    eat[rail[i]] += 1

while l != N:
    ans = max(ans, len(eat))

    eat[rail[l]] -= 1
    if eat[rail[l]] == 0:
        del eat[rail[l]]
    l += 1
    r += 1
    eat[rail[r]] += 1
print(ans)