N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = sorted(B)
A = sorted(A, reverse=True)
sum = 0
for i in range(N):
    sum += A[i] * B[i]
print(sum)