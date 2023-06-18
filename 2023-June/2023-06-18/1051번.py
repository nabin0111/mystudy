N, M = map(int, input().split())
square = []
for _ in range(N):
    square.append(input())

f = min(N, M)
find = False
while True:
    for i in range(N-f+1):
        for j in range(M-f+1):
            if square[i][j] == square[i+f-1][j] == square[i][j+f-1] == square[i+f-1][j+f-1]:
                find = True
                break
        if find:
            break
    if find:
        print(f*f)
        break
    f -= 1