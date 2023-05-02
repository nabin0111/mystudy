N = int(input())
ans = 1
for i in range(N):
    ans += 4 + i*3
    ans %= 45678
print(ans)