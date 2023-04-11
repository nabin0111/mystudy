arr = []
A, B = map(int, input().split())
i = 1
while len(arr) < B:
    arr += [i] * i
    i += 1
print(sum(arr[A-1:B]))