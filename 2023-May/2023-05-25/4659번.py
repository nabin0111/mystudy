import sys
import re
input = sys.stdin.readline
def check(s):
    if re.search(r'[aeiou]', s) is None:
        return False
    v = [i.start() for i in re.finditer(r'[aeiou]', s)]
    c = [i.start() for i in re.finditer(r'[^aeiou]', s)]
    for i in range(1, len(v)-1):
        if v[i-1] + 2 == v[i+1]:
            return False
    for i in range(1, len(c)-1):
        if c[i-1] + 2 == c[i+1]:
            return False
    for i in range(1, len(s)):
        if s[i-1] == s[i] and s[i] != 'e' and s[i] != 'o':
            return False
    return True

while True:
    i = input().rstrip()
    if i == 'end':
        break
    if check(i):
        print(f'<{i}> is acceptable.')
    else:
        print(f'<{i}> is not acceptable.')