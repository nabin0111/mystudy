N = int(input())
balls = input()
rballs = balls[::-1]
R1, B1, R2, B2 = 0, 0, 0, 0
countR1, countB1, countR2, countB2 = False, False, False, False
for i in range(len(balls)):
    if not countR1 and balls[i] == 'B':
        countR1 = True
    elif countR1 and balls[i] == 'R':
        R1 += 1
    
    if not countB1 and balls[i] == 'R':
        countB1 = True
    elif countB1 and balls[i] == 'B':
        B1 += 1

    if not countR2 and rballs[i] == 'B':
        countR2 = True
    elif countR2 and rballs[i] == 'R':
        R2 += 1
    
    if not countB2 and rballs[i] == 'R':
        countB2 = True
    elif countB2 and rballs[i] == 'B':
        B2 += 1
print(min(R1, B1, R2, B2))