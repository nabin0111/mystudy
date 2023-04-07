N = int(input())
five = 0
two = 0
for i in range(N, 0, -1):
    n = i
    while n % 2 == 0:
        two += 1
        n //= 2
    while n % 5 == 0:
        five += 1
        n //= 5
print(min(five, two))