import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

q = [(i, i) for i in range(1, N+1)]
visit = [False] * (N+1)
group = set()
while q:
    cur, g = q.pop()
    if visit[cur]:
        continue
    visit[cur] = True
    group.add(g)

    for v, e in enumerate(graph[cur]):
        if e == 1:
            q.append((v, g))
print(len(group))