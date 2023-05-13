N = int(input())
ans = 1
while N:
    if N == 1:
        break
    if N % 2 == 1:
        ans = 0
        break
    N //= 2
print(ans)