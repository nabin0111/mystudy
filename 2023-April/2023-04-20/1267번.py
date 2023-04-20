N = int(input())
call = list(map(int, input().split()))
y, m = 0, 0
for i in call:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15

if y == m:
    print("Y M", y)
elif y < m:
    print("Y", y)
else:
    print("M", m)