import sys
input = sys.stdin.readline

N = int(input())
stick = []
m = 0
for _ in range(N):
    l, h = map(int, input().split())
    stick.append((l, h))
    if h > m:
        m = h
        loc = (l, h)

stick = sorted(stick, key=lambda x: x[0])
loc = stick.index(loc)
ans = 0
front, back = stick[:loc+1], stick[loc:]
front.reverse()
top = front.pop() if front else 0
while front:
    l, h = front.pop()
    ans += (l - top[0]) * top[1]
    if h > top[1]:
        top = (l, h)
    else:
        top = (l, top[1])
ans += top[1]
top = back.pop() if back else 0
while back:
    l, h = back.pop()
    ans += (top[0] - l) * top[1]
    if h > top[1]:
        top = (l, h)
    else:
        top = (l, top[1])
print(ans)