N, K = map(int, input().split())
d = [1 for x in range(N+1)]
cnt = 0
for i in range(2, N+1):
    if d[i] == 1:
        for j in range(i, N+1, i):
            if d[j] == 1:
                d[j] = 0
                cnt += 1
            if cnt == K:
                print(j)
                break
    if cnt == K:
        break