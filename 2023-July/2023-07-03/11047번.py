import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
ans = 0
while K > 0:
    N -= 1
    c = coins[N]
    
    ans += (K // c)
    K %= c
print(ans)