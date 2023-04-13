n, m = map(int, input().split())
a, b = 1, 1
for i in range(1, m+1):
    a *= n
    b *= i
    n -= 1
print(a//b)