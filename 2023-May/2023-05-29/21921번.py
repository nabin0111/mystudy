N, X = map(int, input().split())
visit = list(map(int, input().split()))
if sum(visit) == 0:
    print('SAD')
else:
    part = [0] + visit
    for i in range(1, N+1):
        part[i] += part[i-1]
    m, cnt = 0, 0
    for i in range(X, N+1):
        cur = part[i] - part[i-X]
        if cur > m:
            m = cur
            cnt = 1
        elif cur == m:
            cnt += 1
    print(m)
    print(cnt)