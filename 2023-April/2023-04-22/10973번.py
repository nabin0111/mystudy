import sys
input = sys.stdin.readline

N = int(input())
perm = list(map(int, input().split()))
idx = -1
for i in range(len(perm)-1, 0, -1):
    if perm[i-1] > perm[i]:
        idx = i-1
        break
if idx == -1:
    print(-1)
else:
    st = perm[idx]
    for i in sorted(perm[idx+1:], reverse=True):
        if i < st:
            st = i
            break
    remain = perm[idx:]
    remain.remove(st)
    result = perm[:idx] + [st] + sorted(remain, reverse=True)
    print(*result)