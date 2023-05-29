N = int(input())
req = list(map(int, input().split()))
M = int(input())
l, r = 0, max(req)
ans = 0
while l <= r:
    mid = (l+r)//2
    cur = 0
    for i in req:
        if i <= mid:
            cur += i
        else:
            cur += mid
    if cur <= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)