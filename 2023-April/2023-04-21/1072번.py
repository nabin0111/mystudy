X, Y = map(int, input().split())
want = ((Y * 100) // X) + 1
if want >= 100:
    print(-1)
else:
    l, r = 1, X
    while l <= r:
        mid = (l + r) // 2
        if ((Y + mid) * 100) // (X + mid) >= want:
            r = mid - 1
        else:
            l = mid + 1
    print(l)
