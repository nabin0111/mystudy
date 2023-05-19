import sys
input = sys.stdin.readline
n = int(input())
num = [0]*n
cur = 1
stack = []
op = []
pos = True
for _ in range(n):
    i = int(input())
    if not pos:
        continue
    while cur <= i:
        stack.append(cur)
        cur += 1
        op.append('+')
    if stack and stack[-1] == i:
        op.append('-')
        stack.pop()
    else:
        pos = False
if pos:
    for i in op:
        print(i)
else:
    print('NO')