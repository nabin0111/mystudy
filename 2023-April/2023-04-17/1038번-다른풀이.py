def dec(list):
    ans = -1
    for i in range(1, len(list)):
        if list[i-1] == list[i]:
            ans = len(list) - (i-1)
            break
    return ans

N = int(input())

n = 0
cnt = -1

while True:
    if n > 9876543210:
        n = -1
        break
    num = list(str(n))
    ans = dec(num)
    if ans == -1:
        cnt += 1
        if cnt == N:
            break
        n += 1
    else:
        ten = 10 ** (ans-1)
        n //= ten
        n += 1
        n *= ten

print(n)