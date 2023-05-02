A, B = map(int, input().split())
def sum(n):
    if n < 0:
        n *= -1
    return n * (n+1) // 2

a, b = min(A, B), max(A, B)
if b < 0:
    b += 1
elif a > 0:
    a -= 1
print(sum(b)-sum(a))