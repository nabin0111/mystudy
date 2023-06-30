import sys
input = sys.stdin.readline

N = int(input())
deq = []
for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push_front":
        deq.insert(0, cmd[1])
    elif cmd[0] == "push_back":
        deq.append(cmd[1])
    elif cmd[0] == "pop_front" and deq:
        print(deq.pop(0))
    elif cmd[0] == "pop_back" and deq:
        print(deq.pop(-1))
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        print(0 if deq else 1)
    elif cmd[0] == "front" and deq:
        print(deq[0])
    elif cmd[0] == "back" and deq:
        print(deq[-1])
    else:
        print(-1)