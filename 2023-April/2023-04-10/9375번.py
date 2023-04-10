T = int(input())
for i in range(T):
    clo = {}
    n = int(input())
    for j in range(n):
        name, kind = input().split()
        if kind in clo:
            clo[kind] += 1
        else:
            clo[kind] = 2
    m = 1
    for j in clo.values():
        m *= j
    print(m-1)