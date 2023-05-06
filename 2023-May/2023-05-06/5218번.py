T = int(input())
for _ in range(T):
    w1, w2 = input().split()
    print('Distances: ', end='')
    for i in range(len(w1)):
        a1, a2 = ord(w1[i]), ord(w2[i])
        if a1 <= a2:
            print(a2-a1, end=' ')
        else:
            print(26+a2-a1, end=' ')
    print()