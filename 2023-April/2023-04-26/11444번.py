P = 1000000007
def mul(X1, X2):
    result = [[0, 0] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += X1[i][k] * X2[k][j] % P
    return result

def power(X, n):
    if n == 1:
        return X
    div = power(X, n//2)
    if n % 2 == 0:
        return mul(div, div)
    else:
        return mul(mul(div, div), X)
    
n = int(input())
X = [[1, 1], [1, 0]]
print(power(X, n)[0][1] % P)