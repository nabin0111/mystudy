import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    result = []
    n = int(input())
    idx = 0
    while n > 0:
        if n % 2 == 1:
            result.append(idx)
        idx += 1
        n //= 2
    print(*result)