def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
A, B = map(int, input().split())
g = gcd(A, B) if A > B else gcd(B,A)
print(f'{g}\n{A*B//g}')