from math import sqrt
N = int(input())
dp = [0, 1, 2, 3]
for i in range(4, N+1):
    r = int(sqrt(i))
    a = min([dp[i - x**2] for x in range(1, r+1)])
    dp.append(a+1)
print(dp[N])