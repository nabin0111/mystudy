n, m = map(int, input().split(':'))
a, b = n, m
while a % b != 0:
    a, b = b, a%b
print(f'{n//b}:{m//b}')