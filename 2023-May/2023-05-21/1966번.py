from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    pri = list(map(int, input().split()))
    o = deque(sorted(pri, reverse=True))
    pri = deque(enumerate(pri))
    ans = 1
    while True:
        if pri[0][1] == o[0]:
            if pri[0][0] == M:
                break
            pri.popleft()
            o.popleft()
            ans += 1
        else:
            pri.rotate(-1)
    print(ans)