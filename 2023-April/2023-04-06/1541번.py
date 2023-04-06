ex = input().split('-')
ans = 0
for i in ex[0].split('+'):
    ans += int(i)
for i in ex[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)