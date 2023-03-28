# dictionary가 list보다 빠르다고 함
# readline이 input보다 빠르다고 함

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pmon = {}
for i in range(N):
    x = input().rstrip()
    pmon[i+1] = x
    pmon[x] = i+1    

for i in range(M):
    target = input().rstrip()
    if target.isdigit():
        print(pmon[int(target)])
    else:
        print(pmon[target])