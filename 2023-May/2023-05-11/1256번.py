def comb(n, r):
    nu, de = 1, 1
    if n - r < r:
        r = n - r
    for i in range(r):
        nu *= (n - i)
        de *= (r - i)
    return nu//de

N, M, K = map(int, input().split())
ans = ''
if K <= comb(N+M, N):
    while True:
        if N == 0 or M == 0:
            ans += 'a' * N
            ans += 'z' * M
            break
        tmp = comb(N+M-1, M)
        if tmp >= K:
            ans += 'a'
            N -= 1
        else:
            K -= tmp
            ans += 'z'
            M -= 1

print(-1 if ans == '' else ans)