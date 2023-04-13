import sys
input = sys.stdin.readline
N = int(input())
sum = 1
for i in range(N):
    sum += int(input()) - 1
print(sum)