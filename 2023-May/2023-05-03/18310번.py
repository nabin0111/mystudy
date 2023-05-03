N = int(input())
house = sorted(list(map(int, input().split())))
mid = (len(house)-1)//2
print(house[mid])