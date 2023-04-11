max = (0, 0)
for i in range(5):
    score = sum(list(map(int, input().split())))
    if score > max[1]:
        max = (i+1, score)
print(max[0], max[1])