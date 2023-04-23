n = int(input())
cnt = n // 5
while (n - cnt * 5) % 2 == 1:
    cnt -= 1
    if cnt == -1:
        break
if cnt != -1:
    cnt += (n - cnt * 5) // 2
print(cnt)