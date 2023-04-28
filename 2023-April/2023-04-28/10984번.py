T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    cre = 0
    for _ in range(N):
        C, G = map(float, input().split())
        total += C*G
        cre += C
    print(f'{int(cre)} {total/cre:.1f}')