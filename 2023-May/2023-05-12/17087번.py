from math import gcd
N, S = map(int, input().split())
A = list(map(int, input().split()))
A = [abs(S-i) for i in A]
print(gcd(*A))