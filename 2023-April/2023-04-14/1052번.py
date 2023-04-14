N, K = map(int, input().split())
tmp = N
while bin(tmp)[2:].count('1') > K:
    tmp += 1
print(tmp - N)