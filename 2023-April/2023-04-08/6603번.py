def lotto(num, choice):
    if len(choice) == 6:
        print(*choice)
    else:
        for i, n in enumerate(num):
            lotto(num[i+1:], choice + [n])            

while True:
    tc = list(map(int, input().split()))
    n = tc[0]

    if n == 0:
        break
    else:
        lotto(tc[1:], [])
    print()