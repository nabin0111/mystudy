N = int(input())
W = []
for i in range(N):
    W.append(int(input()))
W = sorted(W)

result = 0
for i in W:
    if i * N > result:
        result = i * N
    N -= 1
print(result)