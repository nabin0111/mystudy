c = int(input())
div = list(map(int, input().split()))
div = sorted(div)
print(div[0]*div[-1])