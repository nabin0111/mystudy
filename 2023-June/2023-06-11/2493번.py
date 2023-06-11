N = int(input())
height = list(map(int, input().split()))
stack = []

for i in range(len(height)-1, -1, -1):
    cur = height[i]
    if not stack:
        stack.append((cur, i))
        continue
    while stack and stack[-1][0] <= cur:
        h, idx = stack.pop()
        height[idx] = i+1
    stack.append((cur, i))

while stack:
    h, i = stack.pop()
    height[i] = 0
print(*height)