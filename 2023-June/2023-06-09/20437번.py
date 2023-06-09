from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())

    cnt_dict = defaultdict(int)

    for c in W:
        cnt_dict[c] += 1
    
    idx_dict = defaultdict(list)

    for i, c in enumerate(W):
        if cnt_dict[c] < K:
            continue
        idx_dict[c].append(i)
    
    minlen, maxlen = float('inf'), 0

    for k, v in idx_dict.items():
        for i in range(len(v)-K+1):
            tmp = v[i+K-1] - v[i] + 1
            minlen = min(minlen, tmp)
            maxlen = max(maxlen, tmp)

    if maxlen == 0:
        print(-1)
    else:
        print(minlen, maxlen)