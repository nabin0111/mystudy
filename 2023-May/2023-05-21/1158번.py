from collections import deque

N, K = map(int, input().split())
num = deque(list(range(1, N+1)))
res = []
c = 1
while num:
    num.rotate(-(K-1))
    res.append(str(num.popleft()))
print(f"<{', '.join(res)}>")