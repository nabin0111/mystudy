H, W = map(int, input().split())
height = list(map(int, input().split()))

ans = 0
for i in range(1, W-1):
    l, r = max(height[:i]), max(height[i+1:])
    stand = min(l, r)
    if height[i] < stand:
        ans += stand-height[i]
print(ans)