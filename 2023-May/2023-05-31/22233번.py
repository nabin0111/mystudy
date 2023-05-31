import sys
input = sys.stdin.readline
N, M = map(int, input().split())
key = set()
for _ in range(N):
    key.add(input().rstrip())
for _ in range(M):
    post = input().rstrip().split(',')
    for p in post:
        if p in key:
            key.remove(p)
    print(len(key))