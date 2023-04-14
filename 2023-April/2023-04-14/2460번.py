max = 0
cur = 0
for i in range(10):
    off, on = map(int, input().split())
    cur += (on - off)
    if cur > max:
        max = cur
print(max)