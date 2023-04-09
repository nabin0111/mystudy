base, ex, m = map(int, input().split())

def calc(base, ex, m):
    if base == 1 or ex == 1:
        return base % m
    elif ex % 2 == 0:
        r = calc(base, ex // 2, m)
        return (r * r) % m
    else:
        return (base * calc(base, ex - 1, m)) % m

print(calc(base, ex, m))