def gcd(a, b):
    if a % b == 0:
        return b
    if b % a == 0:
        return a
    return gcd(b, a%b)

N = int(input())
tree = []
d = []

for i in range(N):
    tree.append(int(input()))

tree.sort()

g = tree[1]-tree[0]
for i in range(N-1):
    d.append(tree[i+1]-tree[i])
    g = gcd(g, d[i])

sum = 0
for i in range(N-1):
    sum += d[i] / g - 1

print(int(sum))