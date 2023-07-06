num = list(map(int, input().split()))
num.sort()

tmp = num[2]
while True:
    cnt = 0
    for n in num:
        if tmp % n == 0:
            cnt += 1
    if cnt >= 3:
        break
    tmp += 1
print(tmp)