N = int(input())
height = list(map(int, input().split()))
ans = [0] * N

for idx, h in enumerate(height):
    idx += 1
    cnt = h
    for i, a in enumerate(ans):
        if a == 0:
            if cnt == 0:
                ans[i] = idx
                break
            cnt = max(0, cnt-1)
print(*ans)