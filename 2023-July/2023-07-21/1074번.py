N, r, c = map(int, input().split())
ans = 0
while N != 0:
    N -= 1
    cur = (2**N) * (2**N)
    if r < 2**N and c < 2**N:
        continue
    elif r < 2**N and c >= 2**N:
        ans += cur
        c -= 2**N
    elif r >= 2**N and c < 2**N:
        ans += cur * 2
        r -= 2**N
    else:
        ans += cur * 3
        r -= 2**N
        c -= 2**N
print(ans)