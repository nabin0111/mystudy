N, K = map(int, input().split())
num = list(map(int, input().split()))
l, r, cur = 0, 0, 0
max_cnt = 0
cnt = {}
while r < len(num):
    value = num[cur]
    if value in cnt and cnt[value] == K:
        max_cnt = max(max_cnt, r-l)
        while cnt[value] == K:
            cnt[num[l]] -= 1
            l += 1
    else:
        if value in cnt:
            cnt[value] += 1
        else:
            cnt[value] = 1
        r += 1
        cur += 1
print(max(max_cnt, r-l))