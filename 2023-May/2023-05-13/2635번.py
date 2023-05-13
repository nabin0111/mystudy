N = int(input())
num = []
for i in range(N//2, N+1):
    cur, next_n = N, i
    tmp = [cur, next_n]
    while cur - next_n >= 0:
        cur, next_n = next_n, cur-next_n
        tmp.append(next_n)
    if len(tmp) > len(num):
        num = tmp
print(len(num))
print(*num)