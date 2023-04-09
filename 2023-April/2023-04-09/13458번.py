from math import ceil
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
sup = 0
for i in A:
    if i <= B:
        sup += 1
    else:
        sup += ceil((i - B) / C) + 1
print(sup)