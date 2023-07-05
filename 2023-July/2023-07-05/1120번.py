A, B = input().split()
a, b = len(A), len(B)

ans = []
for i in range(b - a + 1):
    cur = 0
    for j in range(a):
        if A[j] != B[j + i]:
            cur += 1
    ans.append(cur)
print(min(ans))