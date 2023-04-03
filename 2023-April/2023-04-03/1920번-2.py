# set을 사용하면 한참 줄일 수 있음
import sys
input = sys.stdin.readline
N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    print(1) if i in A else print(0)