import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input().rstrip()
    stack = []
    right = True
    for c in string:
        if c == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                right = False
                break
    if stack:
        right = False
    
    print("YES" if right else "NO")