sum = 0
for i in range(5):
    s = int(input())
    if s < 40:
        sum += 40
    else:
        sum += s
print(sum//5)
