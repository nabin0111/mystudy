import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    i = input().split()
    if len(i) == 2:
        i[1] = int(i[1])
    if i[0] == 'add':
        S.add(i[1])
    elif i[0] == 'remove':
        if i[1] in S:
            S.remove(i[1])
    elif i[0] == 'check':
        if i[1] in S:
            print(1)
        else:
            print(0)
    elif i[0] == 'toggle':
        if i[1] in S:
            S.remove(i[1])
        else:
            S.add(i[1])
    elif i[0] == 'all':
        S = set(range(1, 21))
    else:
        S = set()