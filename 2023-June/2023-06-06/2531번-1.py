import sys
input = sys.stdin.readline

N, d, k, c = map(int,input().split())
rail = [int(input()) for _ in range(N)]
rail = rail+rail

ans = 0
for i in range(N):
    eat = set()
    for j in range(k):
        eat.add(list[i+j])
    eat.add(c)
    ans = max(ans, len(eat))
print(ans)