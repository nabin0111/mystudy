import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    board = {a:[0, 0, 0] for a in range(1, n+1)} # 점수, 횟수, 시간
    score = [[0] * (k+1) for _ in range(n+1)]
    for time in range(m):
        i, j, s = map(int, input().split())
        cur = score[i][j]
        if cur < s:
            board[i][0] += s - cur
            score[i][j] = s
        board[i][1] += 1
        board[i][2] = time
    board = sorted(board.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))
    for b, cont in enumerate(board):
        if t == cont[0]:
            print(b+1)
            break