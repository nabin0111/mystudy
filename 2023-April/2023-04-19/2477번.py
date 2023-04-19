K = int(input())
num = []
o, e = 0, 0
id_o, id_e = 0, 0
for i in range(6):
    d, l = map(int, input().split())
    num.append(l)
    if i % 2 == 0 and l > e:
        e, id_e = l, i
    elif i % 2 == 1 and l > o:
        o, id_o = l, i
if id_o - id_e == 1 or id_o - id_e == -1:
    id_o = min(id_o, id_e)
else:
    id_o = max(id_o, id_e)
print((o * e  - num[id_o-2] * num[id_o-3]) * K)