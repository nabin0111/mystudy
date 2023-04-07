# list보다 set이 hash를 사용하기 때문에 더 빠르다고 함
N = int(input())
num = set(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

for i in check:
    if i in num:
        print(1, end=' ')
    else:
        print(0, end=' ')