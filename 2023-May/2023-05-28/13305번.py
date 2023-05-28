N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
answer = 0
cur = price[0]
for i in range(N-1):
    cur = min(cur, price[i])
    answer += (dist[i] * cur)
print(answer)