T = int(input())
for _ in range(T):
    num = map(int, input().split())
    num = [i for i in num if i % 2 == 0]
    print(sum(num), min(num))