N = int(input())
ans = 0
for i in range(N):
    s = i * (i+1) // 2
    if N - s <= 0:
        break
    if (N - s) % (i+1) == 0:
        ans += 1
print(ans)