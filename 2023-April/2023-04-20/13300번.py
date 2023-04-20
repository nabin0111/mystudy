import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stud = [[0] * 2 for _ in range(6)]
for i in range(N):
    S, Y = map(int, input().split())
    stud[Y-1][S] += 1

result = 0
for i in stud:
    result += -(-i[0] // K)
    result += -(-i[1] // K)
print(result)