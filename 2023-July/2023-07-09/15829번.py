L = int(input())
string = input()
ans = 0
a = ord('a')
r = 31
M = 1234567891
for i, c in enumerate(string):
    cur = ord(c) - a + 1
    cur *= r ** i
    ans += cur % M
print(ans % M)