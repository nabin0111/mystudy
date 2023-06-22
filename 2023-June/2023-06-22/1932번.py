import sys
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    tri.append(tmp)

for i in range(n-1):
    cur = tri[i]
    tri[i+1][0] += cur[0]
    tri[i+1][-1] += cur[-1]
    for j in range(len(cur)-1):
        add = max(cur[j], cur[j+1])
        tri[i+1][j+1] += add

print(max(tri[n-1]))