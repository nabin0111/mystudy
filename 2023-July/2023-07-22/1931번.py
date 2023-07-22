import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    s, e = map(int, input().split())
    time.append((s, e))
time.sort(key=lambda x: (x[1], x[0]))
t = -1
ans = 0
for s, e in time:
    if s >= t:
        t = e
        ans += 1
print(ans)