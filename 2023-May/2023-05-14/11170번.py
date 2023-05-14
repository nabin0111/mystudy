def count(a, b):
    ans = 0
    for i in range(a, b+1):
        ans += str(i).count('0')
    return ans
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = count(N, M)
    print(ans)