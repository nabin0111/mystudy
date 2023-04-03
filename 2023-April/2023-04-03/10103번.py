n = int(input())
a, b = 100, 100
for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        b -= x
    elif x < y:
        a -= y
print(f'{a}\n{b}')