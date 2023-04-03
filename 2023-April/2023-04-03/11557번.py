import sys
input = sys.stdin.readline

T = int(input())
S, max = "", -1
for i in range(T):
    N = int(input())
    for i in range(N):
        school, L = input().split()
        if int(L) > max:
            max = int(L)
            S = school
    print(S)