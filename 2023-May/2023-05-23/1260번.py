from collections import deque
N, M, V = map(int, input().split())
line = []
for _ in range(M):
    line.append(tuple(map(int, input().split())))

def dfs():
    q = [V]
    visited = [False] * N
    ans = []
    while q:
        cur = q.pop()
        if visited[cur-1]:
            continue
        visited[cur-1] = True
        ans.append(cur)
        con = []
        for l in line:
            if l[0] == cur:
                tmp = l[1]
            elif l[1] == cur:
                tmp = l[0]
            else:
                continue
            
            if not visited[tmp-1]:
                con.append(tmp)
        q += sorted(con, reverse=True)
    return ans

def bfs():
    q = deque([V])
    visited = [False] * N
    ans = []
    while q:
        cur = q.popleft()
        if visited[cur-1]:
            continue
        visited[cur-1] = True
        ans.append(cur)
        con = []
        for l in line:
            if l[0] == cur:
                tmp = l[1]
            elif l[1] == cur:
                tmp = l[0]
            else:
                continue
            
            if not visited[tmp-1]:
                con.append(tmp)
        q += sorted(con)
    return ans

print(*dfs())
print(*bfs())