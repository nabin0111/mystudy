def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

t = int(input())
for i in range(t):
    num = list(map(int, input().split()))
    n = num[0]
    num = sorted(num[1:])
    sum = 0
    for j in range(len(num)-1):
        for k in range(j+1, len(num)):
            sum += gcd(num[j], num[k])
    print(sum)