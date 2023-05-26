N, new, P = map(int, input().split())
score = []
if N != 0:
    score = list(map(int, input().split()))
score.append(new)
score.sort(reverse=True)
rank = score.index(new)+1
if rank+score.count(new)-1 > P:
    print(-1)
else:
    print(rank)