import heapq
import sys
input = sys.stdin.readline
N = int(input())
l_heap = [-int(input())]
r_heap = []
print(-l_heap[0])
for i in range(1, N):
    n = int(input())

    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, -n)
    else:
        heapq.heappush(r_heap, n)
    
    if -l_heap[0] > r_heap[0]:
        l = heapq.heappop(l_heap)
        r = heapq.heappop(r_heap)
        heapq.heappush(l_heap, -r)
        heapq.heappush(r_heap, -l)
    print(-l_heap[0])