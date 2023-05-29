from collections import deque
string = deque(input())
n = 1
while True:
    cur = str(n)
    for c in cur:
        if c == string[0]:
            string.popleft()
        if not string:
            break
    if not string:
        print(n)
        break
    n += 1