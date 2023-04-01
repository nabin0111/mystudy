T = int(input())

for i in range(T):
    line = input().split()
    o = float(line[0])
    for i in line[1:]:
        if i == '@':
            o *= 3
        elif i == '%':
            o += 5
        else:
            o -=7
    print(f'{o:.2f}')