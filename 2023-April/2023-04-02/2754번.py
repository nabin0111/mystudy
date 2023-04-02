grade = input()
score = grade[0]

if score == 'A':
    score = 4.0
elif score == 'B':
    score = 3.0
elif score == 'C':
    score = 2.0
elif score == 'D':
    score = 1.0
else:
    score = 0.0

if len(grade) == 1:
    pass
elif grade[1] == '+':
    score += 0.3
elif grade[1] == '-':
    score -= 0.3

print(score)