from math import ceil

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

day = max(ceil(A / C), ceil(B / D))
print(L - day)