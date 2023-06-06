line = input()
a = line.count('a')
line += line

l, r = 0, a-1
length = len(line)//2
ans = float('inf')
cur = line[:r+1].count('b')
while l < length:
    ans = min(ans, cur)
    if line[l] == 'b':
        cur -= 1
    l += 1
    r += 1
    if line[r] == 'b':
        cur += 1
print(ans)