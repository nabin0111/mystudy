A, B = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))
result = []
total = 0
for i in range(m):
    total += (A ** i) * num[-i-1]
while total:
    result.append(total % B)
    total //= B
print(*result[::-1])