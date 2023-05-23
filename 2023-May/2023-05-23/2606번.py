N = int(input())
M = int(input())
q = [1]
edge = []
for _ in range(M):
    edge.append(tuple(map(int, input().split())))
ans = set()
visit = [False] * (N+1)
while q:
    cur = q.pop()
    visit[cur] = True
    for e in edge:
        if e[0] == cur:
            tmp = e[1]
        elif e[1] == cur:
            tmp = e[0]
        else:
            continue
            
        if not visit[tmp]:
            ans.add(tmp)
            q.append(tmp)
print(len(ans))