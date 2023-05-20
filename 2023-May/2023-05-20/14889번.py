from itertools import combinations

N = int(input())
score = 0
S = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    score += sum(tmp)
    S.append(tmp)

c = list(combinations(range(N), N//2))
part = float('inf')
l = len(c)
for i in range(l//2):
    tmp1, tmp2 = 0, 0
    for a, b in combinations(c[i], 2):
        tmp1 += S[a][b] + S[b][a]
    for a, b in combinations(c[l-1-i], 2):
        tmp2 += S[a][b] + S[b][a]
    part = min(part, abs(tmp1-tmp2))
print(part)