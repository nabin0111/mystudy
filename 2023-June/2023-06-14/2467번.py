N = int(input())
values = list(map(int, input().split()))

ans = float('inf')
l, r = 0, N-1
while l < r:
    tmp = values[l] + values[r]
    if abs(tmp) < abs(ans):
        ans = tmp
        idx = (l, r)
        if ans == 0:
            break
    if tmp < 0:
        l += 1
    else:
        r -= 1
print(values[idx[0]], values[idx[1]])