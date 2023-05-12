D, K = map(int, input().split())
a3, a4 = 1, 1
b3, b4 = 1, 2
for _ in range(D-3):
    a3, a4 = a4, a3+a4
    b3, b4 = b4, b3+b4

for i in range(1, K+1):
    if (K - a3 * i) % b3 == 0:
        A = i
        break
print(A)
print((K - a3 * A) // b3)