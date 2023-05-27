import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    player = input().split()
    team = set([p for p in player if player.count(p) >= 6])
    score = {}
    cur = 1
    for p in player:
        if p in team:
            if p in score:
                score[p] += (cur,)
            else:
                score[p] = (cur,)
            cur += 1

    score = sorted(score.items(), key=lambda x: (sum(x[1][:4]), x[1][4]))
    print(score[0][0])
