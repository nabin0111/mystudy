import sys
input = sys.stdin.readline

N = int(input())
files = []
for _ in range(N):
    files.append(list(input().rstrip()))

ans = files[0]
for i in range(1, N):
    cur = files[i]
    for j in range(len(ans)):
        if ans[j] != cur[j]:
            ans[j] = '?'
print(''.join(ans))