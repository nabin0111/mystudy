import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    cur = list(map(int, input().split()))
    n, scores = cur[0], cur[1:]

    avg = sum(scores) / n
    over = [s for s in scores if s > avg]
    print(f'{100*len(over)/n:.3f}%')