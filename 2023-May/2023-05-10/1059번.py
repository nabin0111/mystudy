L = int(input())
S = list(map(int, input().split()))
S = sorted(S)
n = int(input())
for i in range(L):
    if n == S[i]:
        idx = -1
        break
    if n < S[i]:
        idx = i
        break
ans = 0
if idx != -1:
    if idx == 0:
        s = 1
    else:
        s = S[idx-1] + 1
    e = S[idx] - 1
    for i in range(s, n+1):
        for j in range(max(i+1, n), e+1):
            ans += 1
print(ans)