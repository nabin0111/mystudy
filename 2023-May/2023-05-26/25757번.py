import sys
input = sys.stdin.readline
N, game = input().split()
g = {'Y':1, 'F':2, 'O':3}
u = set()
cnt = 0
for _ in range(int(N)):
    user = input().rstrip()
    if user not in u:
        u.add(user)
        cnt += 1
print(cnt // g[game])