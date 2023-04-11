L, P = map(int, input().split())
num = list(map(int, input().split()))
num = [x - L*P for x in num]
print(*num)