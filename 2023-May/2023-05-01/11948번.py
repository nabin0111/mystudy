A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
a, b = [A, B, C, D], [E, F]
print(sum(a+b)-min(a)-min(b))