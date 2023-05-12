a, b = map(int, input().split())
r = abs((a-1)%4 - (b-1)%4)
c = abs((a-1)//4-(b-1)//4)
print(r+c)