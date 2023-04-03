T = int(input())
for i in range(T):
    a, b = 0, 0
    for i in range(9):
        y, k = map(int, input().split())
        a += y
        b += k
    
    if a == b:
        print("Draw")
    elif a > b:
        print("Yonsei")
    else:
        print("Korea")