import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    i = input().split()
    if i[0] == 'push':
        stack.append(i[1])
    elif i[0] == 'pop' and stack:
        print(stack.pop())
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        print(1 if stack==[] else 0)
    elif stack:
        print(stack[-1])
    else:
        print(-1)