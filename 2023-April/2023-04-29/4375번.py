import sys
lines = sys.stdin.readlines()
for line in lines:
    n = '1'
    while int(n) % int(line):
        n += '1'
    print(len(n))