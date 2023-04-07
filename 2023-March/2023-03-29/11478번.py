S = input()
total = set()

for i in range(1, len(S)+1):
    for j in range(len(S)-i+1):
        total.add(S[j:j+i])
    
print(len(total))