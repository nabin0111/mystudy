from math import gcd
n = int(input())
num = list(map(int, input().split()))
g = gcd(*num)
ans = set()
for i in range(1, int(g**(1/2))+1):
    if g % i == 0:
        ans.add(i)
        ans.add(g//i)
for i in sorted(ans):
    print(i)