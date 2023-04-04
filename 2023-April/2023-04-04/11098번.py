from operator import itemgetter

n = int(input())
for i in range(n):
    info = []
    p = int(input())
    for j in range(p):
        a, b = input().split()
        info.append((float(a), b))
    print(sorted(info, key=itemgetter(0), reverse=True)[0][1])