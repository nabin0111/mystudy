import sys
input = sys.stdin.readline
N = input().rstrip()
l = len(N)
cnt = 0
for i in range(l-1):
    cnt += 9 * (i+1) * (10**i)
cnt += (int(N)-10**(l-1)+1) * l
print(cnt)