N, M = map(int, input().split())
pack, one = 1000, 1000
for _ in range(M):
    p, o = map(int, input().split())
    pack = min(pack, p)
    one = min(one, o)
six = N // 6
ind = N % 6
mix = six * pack + ind * one
all_s = (six+1) * pack if ind != 0 else six * pack
all_i = N * one
print(min(mix, all_s, all_i))