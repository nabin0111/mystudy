import sys
input = sys.stdin.readline

p, m = map(int, input().split())
room = []
for _ in range(p):
    l, n = input().rstrip().split()
    l = int(l)
    f = False
    for r in room:
        if abs(r[0][0] - l) <= 10 and len(r) < m:
            r.append((l, n))
            f = True
            break
    if not f:
        room.append([(l, n)])
for r in room:
    r = sorted(r, key=lambda x: x[1])
    if len(r) == m:
        print('Started!')
    else:
        print('Waiting!')
    for a in r:
        print(*a)