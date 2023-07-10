N = int(input())
time = list(map(int, input().split()))
time.sort()
ans = 0
for t in time:
    ans += t * N
    N -= 1
print(ans)