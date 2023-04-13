sec = [int(input()) for _ in range(4)]
total = sum(sec)
print(f'{total//60}\n{total%60}')