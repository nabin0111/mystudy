N = int(input())
cur = list(map(int, list(input())))
tar = list(map(int, list(input())))
ans = -1

def change(x):
    if x == 1:
        return 0
    else:
        return 1
cnt = 0
tmp = cur[:]
for i in range(1, N):
    if tmp[i-1] != tar[i-1]:
        tmp[i-1] = change(tmp[i-1])
        tmp[i] = change(tmp[i])
        if i+1 < N:
            tmp[i+1] = change(tmp[i+1])
        cnt += 1
if tmp == tar:
    ans = cnt

cnt = 1
tmp = cur[:]
tmp[0] = change(tmp[0])
tmp[1] = change(tmp[1])
for i in range(1, N):
    if tmp[i-1] != tar[i-1]:
        tmp[i-1] = change(tmp[i-1])
        tmp[i] = change(tmp[i])
        if i+1 < N:
            tmp[i+1] = change(tmp[i+1])
        cnt += 1
if tmp == tar:
    if ans == -1:
        ans = cnt
    else:
        ans = min(ans, cnt)

print(ans)