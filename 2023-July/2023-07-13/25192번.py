import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    u = input().rstrip()
    if u == "ENTER":
        users = set()
    elif u not in users:
        ans += 1
        users.add(u)
print(ans)