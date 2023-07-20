N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = {0: 0, 1: 0}

def sol(x, y, size):
    total = 0
    for i in range(x, x+size):
        total += sum(paper[i][y:y+size])
    
    if total == 0 or total == size**2:
        ans[paper[x][y]] += 1
    else:
        sol(x, y, size//2)
        sol(x, y+size//2, size//2)
        sol(x+size//2, y, size//2)
        sol(x+size//2, y+size//2, size//2)

sol(0, 0, N)
print(ans[0])
print(ans[1])