total = 0
max = 0
for i in range(4):
    off, on = map(int, input().split())
    total = total - off + on
    if total > max:
        max = total
print(max)