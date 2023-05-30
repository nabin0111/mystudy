import sys
input = sys.stdin.readline
N = int(input())
first = input().rstrip()
ans = 0
for _ in range(N-1):
    tmp = list(first[:])
    cur = input().rstrip()
    cnt = 0
    for c in cur:
        if c in tmp:
            tmp.remove(c)
        else:
            cnt += 1
    if len(tmp) <= 1 and cnt <= 1:
        ans += 1
print(ans)