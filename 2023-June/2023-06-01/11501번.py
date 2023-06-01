import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))[::-1]
    ans = 0
    m = price[0]
    for i in range(1, len(price)):
        cur = price[i]
        if cur > m:
            m = cur
        else:
            ans += (m - cur)
    print(ans)