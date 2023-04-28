A, P = map(int, input().split())
check = [False] * (4 * 9**5 + 1)
num = []
tmp = A
def calc(n):
    res = 0
    for i in str(n):
        res += int(i) ** P
    return res
while check[tmp] == False:
    check[tmp] = True
    num.append(tmp)
    tmp = calc(tmp)
print(num.index(tmp))