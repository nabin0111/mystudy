w = [4, 2, 3]
while True:
    N = input()
    if N == '0':
        break
    ans = len(N) + 1
    for i in N:
        n = int(i)
        if n >= 2:
            n = 2
        ans += w[n]
    print(ans)