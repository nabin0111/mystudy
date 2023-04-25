M = int(input())
loc = []
for _ in range(M):
    X, Y = map(int, input().split())
    loc.append([X, Y])
loc.sort(key=lambda x: x[1])
s, e = loc[0][1], loc[-1][1]

def check(g):
    m = 0
    for i in range(len(loc)-1):
        x1, y1 = loc[i]
        for j in range(i+1, len(loc)):
            x2, y2 = loc[j]
            m = max(m, abs(y1-g) + abs(y2-g) + abs(x1-x2))
    return m

def search(s, e):
    while s < e:
        t1 = (2*s + e) // 3
        t2 = (s + 2*e) // 3
        a, b = check(t1), check(t2)
        if a > b:
            s = t1 + 1
        elif a == b:
            s = t1
            e = t2
        else:
            e = t2 - 1
    return check(e)
print(search(s, e))