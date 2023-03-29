import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lis = set()
wat = set()

for i in range(N):
    lis.add(input().rstrip())

for i in range(M):
    wat.add(input().rstrip())

lis = lis & wat
print(len(lis))
for i in sorted(lis):
    print(i)