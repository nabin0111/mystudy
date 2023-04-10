N, K = map(int, input().split())
mul = 1
div = 1
for i in range(1, K+1):
    mul *= N
    div *= i
    N -= 1
print((mul//div) % 10007)