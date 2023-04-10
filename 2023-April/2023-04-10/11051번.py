N, K = map(int, input().split())
dp = [[1 for _ in range(i+1)] for i in range(N+1)]

for i in range(2, N+1):
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[N][K] % 10007)