N, W, H = map(int, input().split())
D = (W**2 + H**2) ** (1/2)
for _ in range(N):
    L = int(input())
    if L <= D:
        print('DA')
    else:
        print('NE')