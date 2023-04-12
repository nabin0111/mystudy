def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)
N = int(input())
rings = list(map(int, input().split()))
s = rings[0]
for i in range(1, len(rings)):
    if s > rings[i]:
        g = gcd(s, rings[i])
    else:
        g = gcd(rings[i], s)
    print(f'{s//g}/{rings[i]//g}')