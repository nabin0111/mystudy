n, E, W, S, N = map(int, input().split())
ans = 0.0
def dfs(v, cnt, prob):
    global ans
    for dx, dy, pos in [(1,0,E), (-1,0,W), (0,-1,S), (0,1,N)]:
        tmp = (v[-1][0]+dx, v[-1][1]+dy)
        if tmp in v:
            continue
        if pos == 0:
            continue
        if cnt+1 == n:
            ans += prob*pos
            continue
        dfs(v+[tmp], cnt+1, prob*pos)

dfs([(0,0)], 0, 1)
print(ans / 100 ** n)