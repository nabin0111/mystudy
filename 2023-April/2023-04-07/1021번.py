from collections import deque

N, M = map(int, input().split())
queue = deque(range(1, N+1))
order = list(map(int, input().split()))
cnt = 0
for i in order:
    if queue[0] == i:
        queue.popleft()
        continue
    
    if queue.index(i) <= len(queue)//2:
        rot = -1
    else:
        rot = 1

    while queue[0] != i:
        queue.rotate(rot)
        cnt += 1
    queue.popleft()
print(cnt)