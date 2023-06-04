n, k = map(int, input().split())
dp = [[] for _ in range(max(n+1, 4))]
dp[1].append('1')
dp[2].append('1+1')
dp[2].append('2')
dp[3].append('1+1+1')
dp[3].append('1+2')
dp[3].append('2+1')
dp[3].append('3')
for i in range(4, n+1):
    for j in range(1, 4):
        for line in dp[i-j]:
            dp[i].append(line+'+'+str(j))
if len(dp[n]) >= k:
    dp[n].sort()
    print(dp[n][k-1])
else:
    print(-1)