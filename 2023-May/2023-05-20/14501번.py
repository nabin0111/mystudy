N = int(input())
con = []
for i in range(N):
    t, p = map(int, input().split())
    con.append((i, t, p))
pay = [0]*(N+1)
while con:
    d, t, p = con.pop()
    if d+t > N:
        pay[d] = pay[d+1]
    else:
        pay[d] = max(pay[d+1], pay[d+t]+p)
print(pay[0])