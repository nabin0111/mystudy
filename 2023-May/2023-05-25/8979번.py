N, K = map(int, input().split())
medal = []
for _ in range(N):
    n, g, s, b = map(int, input().split())
    if n == K:
        K = (g, s, b)
    medal.append((g, s, b))
medal.sort(key=lambda x: (-x[0], -x[1], -x[2]))
for i, m in enumerate(medal):
    if m == K:
        print(i+1)
        break