import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()
    if num == '0':
        break

    pal = True
    l = len(num)
    for i in range(l//2):
        if num[i] != num[l-i-1]:
            pal = False
            break
    
    print('yes' if pal else 'no')