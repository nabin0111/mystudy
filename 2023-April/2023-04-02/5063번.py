import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    r, e, c = map(int, input().split())
    e -= c
    if r == e:
        print("does not matter")
    elif r > e:
        print("do not advertise")
    else:
        print("advertise")