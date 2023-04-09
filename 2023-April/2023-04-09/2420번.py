N, M = map(int, input().split())
a = N - M if N > M else M - N
print(abs(a))