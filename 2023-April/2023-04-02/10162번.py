A, B, C = 300, 60, 10
a, b, c = 0, 0, 0
T = int(input())
a = T // 300
T -= 300 * a
b = T // 60
T -= 60 * b
if T % 10 == 0:
    c = T // 10
    print(f'{a} {b} {c}')
else:
    print("-1")