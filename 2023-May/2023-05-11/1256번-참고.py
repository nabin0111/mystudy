N, M, K = map(int, input().split())

arr = [[1]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

if arr[N][M] < K:
    print(-1)
else:
    ans = ''
    while True:
        if N == 0 or M == 0:
            ans += 'a' * N
            ans += 'z' * M
            break
        tmp = arr[N-1][M]
        if tmp >= K:
            ans += 'a'
            N -= 1
        else:
            K -= tmp
            ans += 'z'
            M -= 1
    print(ans)