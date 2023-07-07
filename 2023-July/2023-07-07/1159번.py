import sys
input = sys.stdin.readline

N = int(input())
player = {}
for _ in range(N):
    name = input()
    if name[0] in player:
        player[name[0]] += 1
    else:
        player[name[0]] = 1

ans = [k for k, v in player.items() if v >= 5]
if ans:
    print(''.join(sorted(ans)))
else:
    print("PREDAJA")