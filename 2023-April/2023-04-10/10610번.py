N = input()
sum = 0
for i in N:
    sum += int(i)
if sum % 3 == 0 and '0' in N:
    print(''.join(sorted(N, reverse=True)))
else:
    print(-1)