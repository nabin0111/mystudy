ch, cm, cs = map(int, input().split(':'))
sh, sm, ss = map(int, input().split(':'))
t = (sh-ch)*3600 + (sm-cm)*60 + ss-cs
t = t + 24*3600 if t < 0 else t
sh = t // 3600
sm = (t // 60) % 60
ss = t % 60
print(f'{sh:02}:{sm:02}:{ss:02}')