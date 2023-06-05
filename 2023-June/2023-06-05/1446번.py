import sys
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(N)]
dp = [n for n in range(D+1)]

for i in range(D+1):
    dp[i] = min(dp[i], dp[i-1]+1)

    for s, e, l in graph:
        if s == i and e <= D and dp[i]+l < dp[e]:
            dp[e] = dp[i] + l
print(dp[D])