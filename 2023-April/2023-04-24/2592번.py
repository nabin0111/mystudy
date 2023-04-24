num = []
for _ in range(10):
    n = int(input())
    num.append(n)
num = sorted(num, key=lambda x: num.count(x))
print(sum(num)//10)
print(num[-1])