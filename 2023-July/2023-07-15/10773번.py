import sys
input = sys.stdin.readline

K = int(input())
ans = []
for _ in range(K):
    cur = int(input())
    if cur == 0:
        if ans:
            ans.pop()
    else:
        ans.append(cur)
print(sum(ans))    