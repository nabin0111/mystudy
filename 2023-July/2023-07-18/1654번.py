import sys
input = sys.stdin.readline

K, N = map(int, input().split())
L = []
for _ in range(K):
    L.append(int(input()))

s, e = 1, max(L)
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for li in L:
        cnt += (li // mid)
    
    if cnt >= N:
        s = mid + 1
    else:
        e = mid - 1
print(e)