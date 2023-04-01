import sys
input = sys.stdin.readline

A = int(input())
o = input().rstrip()
B = int(input())

if o == '*':
    print(A*B)
else:
    print(A+B)