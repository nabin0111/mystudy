king, stone, N = input().split()
h = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
v = ['1', '2', '3', '4', '5', '6', '7', '8']
king = [h.index(king[0]), v.index(king[1])]
stone = [h.index(stone[0]), v.index(stone[1])]

def check(h, v):
    if h >= 0 and h <= 7:
        if v >= 0 and v <= 7:
            return True
    return False

for i in range(int(N)):
    hor, ver = 0, 0
    move = input()
    
    if 'R' in move:
        hor += 1
    if 'L' in move:
        hor -= 1
    if 'T' in move:
        ver += 1
    if 'B' in move:
        ver -= 1
    
    if king[0] + hor == stone[0] and king[1] + ver == stone[1]:
        if check(stone[0] + hor, stone[1] + ver):
            king[0] += hor
            king[1] += ver
            stone[0] += hor
            stone[1] += ver
    else:
        if check(king[0] + hor, king[1] + ver):
            king[0] += hor
            king[1] += ver

print(h[king[0]]+v[king[1]])
print(h[stone[0]]+v[stone[1]])