N = int(input())
perm = list(map(int, input().split()))

if perm == sorted(perm, reverse=True):
    print(-1)
else:
    idx = 0
    for i in range(N-1, 0, -1):
        if perm[i-1] < perm[i]:
            idx = i
            break
    result = perm[:idx-1]
    for i in sorted(perm[idx:]):
        if i > perm[idx-1]:
            m = i
            break
    perm.remove(m)
    result.append(m)
    result += sorted(perm[idx-1:])
    print(*result)