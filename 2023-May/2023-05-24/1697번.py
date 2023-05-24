from collections import deque

N, K = map(int, input().split())
q = deque([K])
visit = {K: 0}

while q:
    cur = q.popleft()
    if cur == N:
        print(visit[N])
        break

    a, b, c = cur-1, cur+1, cur//2
    if a >= 0 and a not in visit:
        visit[a] = visit[cur]+1
        q.append(a)
    if b not in visit:
        visit[b] = visit[cur]+1
        q.append(b)
    if cur % 2 == 0 and c not in visit:
        visit[c] = visit[cur]+1
        q.append(c)