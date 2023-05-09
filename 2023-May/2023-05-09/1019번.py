N = input()
num = [0] * 10
idx = len(N)-1
ten = 0

while idx >= 0:
    pre = N[:idx]
    cur = int(N[idx])
    post = N[idx+1:]

    if post != '':
        num[cur] += int(post) + 1
    elif cur != 0:
        num[cur] += 1

    if pre == '':
        pre = '0'

    for i in range(1, cur):
        num[i] += (int(pre)+1) * (10**ten)

    for i in range(cur, 10):
        if i == 0:
            continue
        num[i] += int(pre) * (10**ten)
    
    if cur == 0:
        if idx != len(N)-1:
            num[0] += (int(pre)-1) * (10**ten)
        else:
            num[0] += int(pre) * (10**ten)
    else:
        num[0] += int(pre) * (10**ten)

    ten += 1
    idx -= 1
print(*num)