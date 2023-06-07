S = input()
T = input()

ans = 0
def change(x, reverse):
    global ans
    if ans == 1:
        return
    if len(x) == len(S):
        if reverse % 2 == 1:
            x = x[::-1]
        if x == S:
            ans = 1
        return
    
    if reverse % 2 == 0:
        if x[-1] == 'A':
            change(x[:-1], reverse)
        if x[0] == 'B':
            change(x[1:], reverse+1)
    else:
        if x[0] == 'A':
            change(x[1:], reverse)
        if x[-1] == 'B':
            change(x[:-1], reverse+1)

change(T, 0)
print(ans)