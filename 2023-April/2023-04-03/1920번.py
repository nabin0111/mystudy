# 시간초과 때문에 애먹음 binary search 사용
# 단, slicing은 복사이기 때문에 시간 단축 안 됨
import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

def bs(t):
    global A, N
    s, f = 0, N-1
    while s <= f:
        n = (s+f+1)//2
        if A[n] == t:
            return 1
        elif t < A[n]:
            f = n-1
        else:
            s = n+1
    return 0


M = int(input())
B = list(map(int, input().split()))
for i in B:
    print(bs(i))