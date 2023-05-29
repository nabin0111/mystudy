import sys
input = sys.stdin.readline
N, M = map(int, input().split())
words = {}
for _ in range(N):
    i = input().rstrip()
    if len(i) >= M:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1

for i, j in sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(i)