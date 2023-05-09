num = input()
if len(num) == 2:
    a, b = int(num[0]), int(num[1])
elif len(num) == 3:
    if num[1] == '0':
        a, b = int(num[:2]), int(num[2])
    else:
        a, b = int(num[0]), int(num[1:])
else:
    a, b = int(num[:2]), int(num[2:])
print(a+b)