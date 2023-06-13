from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = deque([(1, 0)])
dist = [float('inf')] * (N+1)
dist[1] = 0
while q:
    cur, cow = q.popleft()
    if dist[cur] < cow:
        continue
    for g in graph[cur]:
        tmp = cow + g[1]
        if tmp < dist[g[0]]:
            dist[g[0]] = tmp
            q.append((g[0], tmp))
print(dist[N])