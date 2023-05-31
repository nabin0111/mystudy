import sys
input = sys.stdin.readline
N, M = map(int, input().split())
name, value = [], []
for _ in range(N):
    n, v = input().split()
    v = int(v)
    name.append(n)
    value.append(v)
for _ in range(M):
    tar = int(input())
    l, r = 0, len(value)-1
    while l <= r:
        mid = (l+r)//2
        cur = value[mid]
        if cur < tar:
            l = mid + 1
        else:
            r = mid -1
    print(name[l])