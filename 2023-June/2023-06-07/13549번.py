from collections import deque

N, K = map(int, input().split())
q = deque([N])
loc = [float('inf')] * (200002)
loc[N] = 0
while q:
    cur = q.popleft()

    if cur == K:
        print(loc[K])
        break

    m1, m2, m3 = cur-1, cur+1, cur*2

    if m1 >= 0 and loc[m1] > loc[cur]+1:
        loc[m1] = loc[cur] + 1
        q.append(m1)
    
    if m2 <= 200001 and loc[m2] > loc[cur]+1:
        loc[m2] = loc[cur] + 1
        q.append(m2)
    
    if m3 < 200001 and loc[m3] > loc[cur]:
        loc[m3] = loc[cur]
        q.appendleft(m3)