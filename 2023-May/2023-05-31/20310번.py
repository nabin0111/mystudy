S = list(input())
a, b = S.count('0')//2, S.count('1')//2
idx = 0
while b:
    if S[idx] == '1':
        S.pop(idx)
        b -= 1
    else:
        idx += 1
idx = len(S) - 1
while a:
    if S[idx] == '0':
        S.pop(idx)
        a -= 1
    idx -= 1
print(''.join(S))