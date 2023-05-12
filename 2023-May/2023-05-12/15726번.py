num = list(map(int, input().split()))
big = max(num[1], num[2])
small = min(num[1], num[2])
print(num[0]*big//small)