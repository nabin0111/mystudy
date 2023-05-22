N, S = map(int, input().split())
num = list(map(int, input().split()))
ans = 0

def check(cnt, cur):
    global ans
    if cnt == N:
        if cur == S:
            ans += 1
    else:
        check(cnt+1, cur+num[cnt])
        check(cnt+1, cur)
check(0, 0)
print(ans-1 if S == 0 else ans)