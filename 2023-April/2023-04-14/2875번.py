from math import ceil
N, M, K = map(int, input().split())
if N > 2 * M:
    team = M
    K -= (N - 2 * M)
else:
    team = N // 2
    K -= (M - team)
if K > 0:
    team -= ceil(K / 3)
print(team)