def pascal(n, k):
    if k > n - k:
        k = n - k
    nu, de = 1, 1
    for i in range(k):
        nu *= (n - i)
        de *= (k - i)
    return nu//de
n, k = map(int, input().split())
print(pascal(n-1, k-1))