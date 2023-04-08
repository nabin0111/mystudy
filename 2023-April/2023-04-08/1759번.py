def password(chars, L, cur, v, c):
    if len(cur) == L:
        if v >= 1 and c >= 2:
            print(cur)
    else:
        for i, char in enumerate(chars):
            if char in ['a', 'e', 'i', 'o', 'u']:
                password(chars[i+1:], L, cur+char, v+1, c)
            else:
                password(chars[i+1:], L, cur+char, v, c+1)

L, C = map(int, input().split())
chars = list(input().split())
chars = sorted(chars)
password(chars, L, "", 0, 0)