from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop' and q:
        print(q.popleft())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(0 if q else 1)
    elif cmd[0] == 'front' and q:
        print(q[0])
    elif cmd[0] == 'back' and q:
        print(q[-1])
    else:
        print(-1)