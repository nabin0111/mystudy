from itertools import permutations

N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
op = [0]*add+[1]*sub+[2]*mul+[3]*div
res_min, res_max = float('inf'), float('-inf')
for p in set(permutations(op, N-1)):
    cur = num[0]
    for i, o in enumerate(p):
        if o == 0:
            cur += num[i+1]
        elif o == 1:
            cur -= num[i+1]
        elif o == 2:
            cur *= num[i+1]
        elif cur >= 0:
            cur //= num[i+1]
        else:
            cur = -(-cur // num[i+1])
    res_min = min(res_min, cur)
    res_max = max(res_max, cur)
print(f'{res_max}\n{res_min}')