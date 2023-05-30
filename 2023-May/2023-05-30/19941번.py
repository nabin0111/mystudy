N, K = map(int, input().split())
string = list(input())
ans = 0
for i, c in enumerate(string):
    if c == 'P':
        for j in range(max(0, i-K), min(N, i+K+1)):
            if string[j] == 'H':
                string[j] = 'N'
                ans += 1
                break
print(ans)