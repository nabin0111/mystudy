T = int(input())
edge = [1, 1, 1]
for i in range(T):
    N = int(input())
    for j in range(len(edge), N):
        edge.append(edge[j-3] + edge[j-2])
    print(edge[N-1])