N = int(input())
K = 1
t = 0
while N:
    if K > N:
        K = 1
    else:
        N -= K
        K += 1
        t += 1
print(t)