import sys
input = sys.stdin.readline

n = int(input())
dif = []
for _ in range(n):
    dif.append(int(input()))

dif.sort()
val = int(n*0.15 + 0.5)
dif = dif[val:n-val]
print(int(sum(dif)/(n-2*val)+0.5) if n else 0)