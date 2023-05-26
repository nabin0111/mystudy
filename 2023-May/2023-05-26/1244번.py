N = int(input())
state = [0] + list(map(int, input().split()))
stu = int(input())
for _ in range(stu):
    s, num = map(int, input().split())
    if s == 1:
        for i in range(num, N+1, num):
            state[i] = 0 if state[i] == 1 else 1
    else:
        for i in range(0, min(N-num, num-1)+1):
            tmp = state[num-i]
            if tmp != state[num+i]:
                break
            state[num-i] = 0 if tmp == 1 else 1
            state[num+i] = state[num-i]
for i in range(1, len(state), 20):
    print(*state[i:i+20])