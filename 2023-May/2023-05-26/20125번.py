import sys
input = sys.stdin.readline
N = int(input())
a, b, c, d, e = 0, 0, 0, 0, 0
heart = None
for i in range(N):
    cur = input().rstrip()
    if '*' not in cur:
        continue
    idx = cur.index('*')
    cnt = cur.count('*')
    if heart is None:
        if cnt == 1:
            heart = (i+1, idx)
        continue
    else:
        if i == heart[0]:
            a = heart[1] - idx
            b = cnt - a - 1
        elif idx == heart[1]:
            c += 1
        elif idx == heart[1] - 1:
            d += 1
            if cnt == 2:
                e += 1
        else:
            e += 1
print(heart[0]+1, heart[1]+1)
print(a, b, c, d, e)