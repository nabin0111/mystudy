V = int(input())
R = input()

a = R.count('A')
b = R.count('B')

if a == b:
    print("Tie")
elif a > b:
    print("A")
else:
    print("B")