N = int(input())
num = set(map(int, input().split()))

print(*sorted(list(num)))