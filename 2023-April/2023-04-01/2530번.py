A, B, C = map(int, input().split())
D = int(input())
D += A*3600 + B*60 + C
C = D % 60
B = (D // 60) % 60
A = (D // 3600) % 24

print(A, B, C)