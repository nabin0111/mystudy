A, B = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

n = gcd(A, B) if A > B else gcd(B, A)
print('1'*n)