prices = []
total = int(input())
for i in range(9):
    prices.append(int(input()))
print(total-sum(prices))