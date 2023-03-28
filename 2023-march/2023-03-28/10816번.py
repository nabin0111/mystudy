import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
num = {}

for i in cards:
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1

M = int(input())
cards = list(map(int, input().split()))
for i in cards:
    if i not in num:
        print(0, end=' ')
        continue
    print(num[i], end=' ')