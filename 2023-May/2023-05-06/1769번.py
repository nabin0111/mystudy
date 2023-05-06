import sys
input = sys.stdin.readline
x = input().rstrip()
ans = 0
while len(x) > 1:
    ans += 1
    y = 0
    for i in x:
        y += int(i)
    x = str(y)
print(ans)
print('YES' if int(x) == 3 or int(x) == 6 or int(x) == 9 else 'NO')