from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    i = int(input())
    if i == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, i)