N, B = map(int, input().split())
result = ""
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N > 0:
    result += tmp[N%B]
    N //= B
# tmp로 시간 줄여서인지(?) 채점됨
print(result[::-1])