# 에라토스테네스의 체 활용 - 파이썬이 훨씬 수월
# 시간 넘 길게 걸림 줄일 수 있으면 줄이기

primes = [False, False] + [True] * 999999

for i in range(2, 1000001):
    if primes[i]:
        for j in range(2*i, 1000001, i):
            primes[j] = False

T = int(input())
for i in range(T):
    cnt = 0
    N = int(input())
    for j in range(2, N//2+1):
        if primes[j] and primes[N-j]:
            cnt += 1
    print(cnt)