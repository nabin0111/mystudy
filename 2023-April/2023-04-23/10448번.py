T = int(input())
pas = [i * (i+1) // 2 for i in range(1, 46)]
def check(n):
    l = len(pas)
    for i in range(l):
        for j in range(i, l):
            for k in range(j, l):
                if pas[i] + pas[j] + pas[k] == n:
                    return 1
    return 0


for i in range(T):
    K = int(input())
    print(check(K))