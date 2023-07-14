import sys
input = sys.stdin.readline

pair = {')': '(', ']': '['}
while True:
    S = input().rstrip()
    if S == ".":
        break

    bal = True
    stack = []
    for c in S:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' or c == ']':
            if stack and stack[-1] == pair[c]:
                stack.pop()
            else:
                bal = False
                break
    if stack:
        bal = False
    print('yes' if bal else 'no')