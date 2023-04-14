import sys
input = sys.stdin.readline

prime_num = [0, 0, 1] + [1, 0] * 499999

for i in range(3, 1000, 2):
    if prime_num[i] == 1:
        for j in range(2*i, 1000000, i):
            prime_num[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    for i in range(3, n//2 + 1, 2):
        if prime_num[i] == 1 and prime_num[n-i] == 1:
            ans = i
            break
    if ans != 0:
        print(f'{n} = {ans} + {n-ans}')
    else:
        print("Goldbach's conjecture is wrong.")
