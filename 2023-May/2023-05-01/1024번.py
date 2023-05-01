N, L = map(int, input().split())
check = [i*(i+1)//2 for i in range(100)]
ans = [-1]
for i in range(L-1, 100):
    if N < check[i]:
        break
    elif (N-check[i])%(i+1) == 0:
        s = (N-check[i])//(i+1)
        ans = list(range(s, s+i+1))
        break
print(*ans)