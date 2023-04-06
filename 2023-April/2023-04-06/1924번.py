x, y = map(int, input().split())
m = [3 for i in range(12)]
m[1] = 0
m[3], m[5], m[8], m[10] = 2, 2, 2, 2
d = 0
w = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
for i in range(x-1):
    d += m[i]
print(w[(d+y-1)%7])