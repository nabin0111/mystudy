n, m = map(int, input().split())
if (n+m) % 2 != 0 and (n-m) % 2 != 0:
    print(-1)
elif n < m:
    print(-1)
else:
    print((n+m)//2, (n-m)//2)