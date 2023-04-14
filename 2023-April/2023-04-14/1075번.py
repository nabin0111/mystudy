import sys
input = sys.stdin.readline

N = int(input()[:-3]+'00')
F = int(input())

r = N % F
if r > 0:
    r = F - r
print(f'{r:02}')