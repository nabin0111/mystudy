import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    num = list(map(int, input().split()))
    for n in num:
        if len(h) < N:
            heappush(h, n)
        elif h[0] < n:
            heappop(h)
            heappush(h, n)
print(h[0])