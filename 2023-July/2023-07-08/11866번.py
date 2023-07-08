N, K = map(int, input().split())
num = list(range(1, N+1))
ans = []
while num:
    for i in range(1, K):
        c = num.pop(0)
        num.append(c)
    ans.append(str(num.pop(0)))
print(f"<{', '.join(ans)}>")