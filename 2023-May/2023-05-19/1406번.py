import sys
input = sys.stdin.readline

front = list(input().rstrip())
back = []

M = int(input())
for _ in range(M):
    i = input().split()
    if i[0] == 'L':
        if front:
            back.append(front.pop())
    elif i[0] == 'D':
        if back:
            front.append(back.pop())
    elif i[0] == 'B':
        if front:
            front.pop()
    else:
        front.append(i[1])
    
print(''.join(front+back[::-1]))