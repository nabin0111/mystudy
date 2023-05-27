from math import ceil
N = int(input())
M = int(input())
x = list(map(int, input().split()))
d = x[0]
for i in range(1, len(x)):
    d = max(d, (x[i]-x[i-1])/2)
d = max(d, N-x[-1])
print(ceil(d))