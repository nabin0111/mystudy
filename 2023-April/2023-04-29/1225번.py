A, B = input().split()
ans = 0
B = sum(list(map(int, list(B))))
for i in A:
    ans += int(i) * B
print(ans)