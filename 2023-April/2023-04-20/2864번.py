A, B = input().split()
A_s, B_s = A.replace('5', '6'), B.replace('5', '6')
A_f, B_f = A.replace('6', '5'), B.replace('6', '5')

print(int(A_f) + int(B_f), int(A_s) + int(B_s))