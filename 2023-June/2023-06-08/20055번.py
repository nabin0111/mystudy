from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = deque(map(int, input().split()))
cnt = 1
robot = deque([False] * N)
while True:
    a.rotate(1)
    robot.rotate(1)
    robot[-1] = False

    if True in robot:
        for i in range(N-2, -1, -1):
            if robot[i]:
                if not robot[i+1] and a[i+1] > 0:
                    robot[i] = False
                    robot[i+1] = True
                    a[i+1] -= 1
        robot[-1] = False
    
    if a[0] > 0:
        robot[0] = True
        a[0] -= 1
    
    if a.count(0) >= K:
        break
    cnt += 1
print(cnt)