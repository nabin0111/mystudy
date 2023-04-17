from itertools import combinations
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
decrease = []

for i in range(1, 11):
    for j in list(combinations(num, i)):
        n = ''.join(sorted(j, reverse=True))
        decrease.append(int(n))

N = int(input())
decrease = sorted(decrease)
print(decrease[N]) if N <= len(decrease)-1 else print(-1)
