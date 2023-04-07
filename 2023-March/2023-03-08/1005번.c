#include <stdio.h>
#include <string.h>

int T, N, K;
int D[1001];
int graph[1001][1001];
int dp[1001]; // 참고

int time(int x) {
    if (dp[x] != -1) { // 0이냐 -1이냐로 갈림
        return dp[x];
    }

    int max = 0;
    for (int i=1;i<=N;i++) {
        if (graph[i][x]) {
            if (time(i) > max) {

                max = dp[i];
            }
        }
    }

    return dp[x] = max + D[x];
}

int main() {
    int W;

    scanf ("%d", &T);

    while (T--) {
        scanf("%d %d", &N, &K);

        memset(dp, -1, sizeof(dp));
        memset(D, 0, sizeof(D));
        memset(graph, 0, sizeof(graph));

        for (int i=1;i<=N;i++) {
            scanf("%d", &D[i]);
        }

        int X, Y;
        for (int i=1;i<=K;i++) {
            scanf("%d %d", &X, &Y);
            graph[X][Y] = 1;
        }

        scanf("%d", &W);
        printf("%d\n", time(W));
    }

    return 0;
}