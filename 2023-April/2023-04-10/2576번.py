odd = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        odd.append(a)
if odd:
    print(f'{sum(odd)}\n{sorted(odd)[0]}')
else:
    print(-1)