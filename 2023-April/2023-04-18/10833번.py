N = int(input())
a = 0
for _ in range(N):
    stu, app = map(int, input().split())
    a += app % stu
print(a)