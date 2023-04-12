def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

T = int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())
    lcm = M * N // gcd(M, N)
    result = -1
    for j in range(x, lcm + 1, M):
        if (j - y) % N == 0:
            result = j
            break
    print(result)