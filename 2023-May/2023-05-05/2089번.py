N = int(input())
ans = ''
if N == 0:
    ans += '0'
N *= -1
while N != 0:
    ans += str(-(N % -2))
    N //= -2
print(ans[::-1])