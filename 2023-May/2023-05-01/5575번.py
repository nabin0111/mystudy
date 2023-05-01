def calc(t):
    total = (t[3]-t[0])*60*60
    total += (t[4]-t[1])*60
    total += t[5]-t[2]
    s = total%60
    total //= 60
    return total//60, total%60, s

for _ in range(3):
    time = list(map(int, input().split()))
    h, m, s = calc(time)
    print(h, m, s)