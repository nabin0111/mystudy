from collections import deque

prime = [False, False, True] + [True, False] * 4999
for i in range(3, 9998, 2):
    if prime[i]:
        for j in range(2*i, 10000, i):
            prime[j] = False

def check(s, e):
    queue = deque([[s, 0]])
    visited = [False] * 10000
    visited[s] = True

    while queue:
        cur, ord = queue.popleft()
        if cur == e:
            return ord
        
        cur = str(cur)
        for i in range(4):
            for j in range(10):
                n = int(cur[:i] + str(j) + cur[i+1:])
                if not visited[n] and prime[n] and n >= 1000:
                    visited[n] = True
                    queue.append([n, ord+1])
    return -1

T = int(input())
for _ in range(T):
    s, e = map(int, input().split())
    result = check(s, e)
    print(result if result != -1 else "Impossible")
