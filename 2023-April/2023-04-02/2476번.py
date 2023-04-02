import sys
input = sys.stdin.readline

max = 0
N = int(input())
for i in range(N):
    e = list(map(int, input().split()))
    e.sort()
    if e[0] == e[2]:
        tmp = 10000 + 1000 * e[0]
    elif e[0] == e[1] or e[1] == e[2]:
        tmp = 1000 + 100 * e[1]
    else:
        tmp = 100 * e[2]
    
    if max < tmp:
        max = tmp
print(max)