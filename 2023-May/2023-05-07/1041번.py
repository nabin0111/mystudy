N = int(input())
die = list(map(int, input().split()))
if N == 1:
    print(sum(die) - max(die))
else:
    two = 100
    for i in range(5):
        for j in range(i+1, 6):
            if i + j == 5:
                continue
            tmp = die[i] + die[j]
            if tmp < two:
                two = tmp
    three = min(die[0], die[5])
    m = 100
    for a, b in [(1, 3), (3, 4), (4, 2), (2, 1)]:
        tmp = die[a] + die[b]
        if tmp < m:
            m = tmp
    three += m
    print(4*three + (4 + 8 * (N-2))*two + (N-2) * (5*N - 6) * min(die))