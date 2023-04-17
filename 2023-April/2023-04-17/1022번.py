import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
paper = [[1] * (c2-c1+1) for _ in range(r2-r1+1)]
total = (c2-c1+1) * (r2-r1+1)
num = 1 # 숫자
paper_cnt = 0
x, y = 0, 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1 ,0]
idx = 0 # dx, dy 의 인덱스
line = 1 # 해당 단계에서 이동해야 할 횟수
cnt = 0 # 해당 단계에서 이동한 횟수

while True:
    if r1 <= x <= r2 and c1 <= y <= c2:
        paper[x-r1][y-c1] = num
        paper_cnt += 1
        if paper_cnt == total:
            break

    x += dx[idx]
    y += dy[idx]
    cnt += 1
    num += 1
    if cnt % line == 0:
        idx = (idx + 1) % 4
        if cnt > line:
            line += 1
            cnt = 0

l = len(str(num))# 가장 큰 수의 길이
for i in paper:
    for j in i:
        print(f'{j:>{l}}', end=' ')
    print()