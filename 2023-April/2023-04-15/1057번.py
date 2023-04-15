N, K, L = map(int, input().split())
cnt, two = 1, 2
K -= 1
L -= 1
while K//two != L//two:
    cnt += 1
    two *= 2
print(cnt)