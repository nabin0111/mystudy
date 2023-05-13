N = int(input())

def check(n):
    for i in str(n):
        if i != '4' and i != '7':
            return False
    return True

while not check(N):
    N -= 1
print(N)