def count(x, c):
    cnt = 0
    while x != 0:
        x //= c
        cnt += x
    return cnt

n, m = map(int, input().split())
five = count(n, 5) - count(m, 5) - count(n-m, 5)
two = count(n, 2) - count(m, 2) - count(n-m, 2)
print(min(five, two))