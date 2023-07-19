import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = []
for _ in range(N):
    blocks += list(map(int, input().split()))

ans_time = float('inf')
ans_h = blocks[0]
n_blocks = sum(blocks)
for i in range(max(blocks), min(blocks)-1, -1):
    if n_blocks + B >= i * N * M:
        t = 0
        for b in blocks:
            task = b - i
            if task >= 0:
                t += 2 * task
            else:
                t -= task
        
        if t < ans_time:
            ans_time = t
            ans_h = i
print(ans_time, ans_h)