N, B = input().split()
B = int(B)
# string reverse 방법
N = N[::-1]

result = 0
for i in range(len(N)):
    if N[i].isdigit():
        result += int(N[i]) * (B**i)
    else:
        # ascii code는 python 함수 ord()를 사용
        result += (ord(N[i]) - ord('A') + 10) * (B**i)

print(result)