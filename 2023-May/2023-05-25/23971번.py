H, W, N, M = map(int, input().split())
ver = (H-1)//(N+1)+1
hor = (W-1)//(M+1)+1
print(ver*hor)