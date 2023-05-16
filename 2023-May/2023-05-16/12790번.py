T = int(input())
for _ in range(T):
    n = list(map(int, input().split()))
    hp = max(n[0]+n[4], 1)
    mp = max(n[1]+n[5], 1)
    att = max(n[2]+n[6], 0)
    d = n[3]+n[7]
    print(hp+5*mp+2*att+2*d)