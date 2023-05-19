from collections import deque

T = int(input())
for _ in range(T):
    f = input()
    n = int(input())
    deq = deque(input()[1:-1].split(','))
    if f.count('D') > n:
        print('error')
        continue
    front = 1
    for i in f:
        if i == 'R':
            front *= -1
        elif front == 1:
            deq.popleft()
        else:
            deq.pop()
    if front == -1:
        deq = reversed(deq)
    print(f"[{','.join(deq)}]")