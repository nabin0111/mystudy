top = input()
h = 10

for i in range(1, len(top)):
    if top[i] == top[i-1]:
        h += 5
    else:
        h += 10
print(h)