n = []
for _ in range(5):
    n.append(int(input()))
ans = 0
if n[0] < 0:
    ans += (0-n[0]) * n[2]
    ans += n[3]
    n[0] = 0
ans += (n[1] - n[0]) * n[4]
print(ans)