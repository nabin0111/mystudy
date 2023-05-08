N = input()
num = [0] * 10
idx = len(N)-1
ten = 0
while idx > 0:
    pre = int(N[:idx])
    cur = int(N[idx])
    a, b = (pre+1) * (10**ten), pre * (10**ten)
    for i in range(1, cur+1):
        num[i] += a
    for i in range(cur+1, 10):
        num[i] += b
    num[0] += b
    idx -= 1
    ten += 1

for i in range(1, int(N[0])+1):
    idx = 1
    res = ''
    cur = 0
    small = False
    while idx < len(N):
        if i < int(N[idx]):
            small = True
            res += N[idx:]
            cur += int(res)
            res = ''
        elif not small and i == int(N[idx]):
            res += '9'
        elif i > int(N[idx]):
            
        idx += 1


print(*num)