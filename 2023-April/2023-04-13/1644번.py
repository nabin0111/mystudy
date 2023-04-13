N = int(input())
prime = [0, 0] + [1] * (N-1)
for i in range(2, N+1):
    if prime[i] == 1:
        for j in range(2*i, N+1, i):
            if prime[j] == 1:
                prime[j] = 0
p = [idx for idx, n in enumerate(prime) if n == 1]
cnt = 0
s, e = 0, 0
while e <= len(p):
    total = sum(p[s:e])
    if total == N:
        cnt += 1
        e += 1
    elif total < N:
        e += 1
    else:
        s += 1
print(cnt)