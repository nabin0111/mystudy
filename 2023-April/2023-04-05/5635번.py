n = int(input())
stud = []
for i in range(n):
    n, d, m, y = input().split()
    stud.append((n, int(y), int(m), int(d)))

stud = sorted(stud, key=lambda x : (x[1], x[2], x[3]))
print(f'{stud[-1][0]}\n{stud[0][0]}')