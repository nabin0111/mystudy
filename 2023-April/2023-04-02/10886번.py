N = int(input())
cnt = 0
for i in range(N):
    cnt += int(input())

if cnt > N // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")