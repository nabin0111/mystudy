ans = 0
for i in range(8):
    cur = input()
    if i % 2 == 0:
        cnt = [cur[i] for i in range(0, 8, 2)]
    else:
        cnt = [cur[i] for i in range(1, 8, 2)]
    ans += cnt.count('F')
print(ans)