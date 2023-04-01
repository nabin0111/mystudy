S = int(input())
c = 0
i = 1
while S > 0:
    if S < i:
        break
    S -= i
    c += 1
    i += 1

print(c)