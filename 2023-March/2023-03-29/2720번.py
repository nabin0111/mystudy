T = int(input())
for i in range(T):
    C = int(input())
    x = C // 25
    C -= 25 * x
    print(x, end=' ')
    x = C // 10
    C -= 10 * x
    print(x, end=' ')
    x = C // 5
    C -= 5 * x
    print(x, C)