num = list(map(int, input().split()))
s = sum([x**2 for x in num])
print(s%10)