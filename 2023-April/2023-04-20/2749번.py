def fib(n):
    a, b = 0, 1

    for _ in range(n-1):
        a, b = b % 1000000, (a + b) % 1000000
    
    return b
n = int(input())
print(fib(n % 1500000))