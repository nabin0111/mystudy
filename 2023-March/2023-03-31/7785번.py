import sys
input = sys.stdin.readline

n = int(input())
cur = set()

for i in range(n):
    name, state = input().split()
    if name in cur:
        cur.remove(name)
    else:
        cur.add(name)

for i in sorted(cur, reverse=True):
    print(i)