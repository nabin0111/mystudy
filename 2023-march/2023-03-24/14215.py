a, b, c = map(int, input().split())
bar = sorted([a, b, c])

while bar[0] + bar[1] <= bar[2]:
    bar[2] -= 1

print(bar[0]+bar[1]+bar[2])