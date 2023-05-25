import sys
input = sys.stdin.readline
P = int(input())
for _ in range(P):
    i = list(map(int, input().split()))
    T, height = i[0], i[1:]
    stack = [height[0]]
    idx = 1
    ans = 0
    while len(stack) != len(height):
        cur = height[idx]
        for a in range(idx-1, -1, -1):
            if stack[a] < cur:
                stack.insert(a+1, cur)
                break
            ans += 1
            if a == 0:
                stack.insert(0, cur)
                break
        idx += 1
    print(T, ans)