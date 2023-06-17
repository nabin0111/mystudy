import sys
input = sys.stdin.readline

check = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 5, 8),
         (0, 4, 8), (2, 4, 6)]

while True:
    game = input().rstrip()
    if game == 'end':
        break

    x, o, dot = game.count('X'), game.count('O'), game.count('.')

    ans = True
    if x != o and x != o+1:
        ans = False
    
    kind, loc = set(), set()
    for a, b, c in check:
        if game[a] != '.' and game[a] == game[b] == game[c]:
            loc |= {a, b, c}
            kind.add(game[a])
    
    if len(kind) == 2:
        ans = False
    elif x == o and 'X' in kind:
        ans = False
    elif x == o+1 and 'O' in kind:
        ans = False
    elif len(loc) > 5:
        ans = False

    if len(loc) == 0 and dot:
        ans = False
    
    if ans:
        print('valid')
    else:
        print('invalid')