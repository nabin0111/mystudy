#include <stdio.h>
#include <memory.h>
#include <math.h>

int T, N;
int dots[20][2];
int visited[20];
double result;
double x, y;

double calc(double x, double y) {
    for (int i=0;i<N;i++) {
        if (visited[i]) {
            x -= (2 * dots[i][0]);
            y -= (2 * dots[i][1]);
        }
    }
    
    return sqrt((x * x) + (y * y));
};

void dfs(int cur, int cnt) {
    double tmp;
    if (cnt == N/2) {
        tmp = calc(x, y);
        if (tmp < result) {
            result = tmp;
        }
        return;
    }

    for (int i=cur;i<N;i++) {
        visited[i] = 1;
        dfs(i+1, cnt+1);
        visited[i] = 0;
    }
};

int main() {
    scanf("%d", &T);

    while (T--) {
        memset(visited, 0, sizeof(visited));
        x = 0;
        y = 0;
        result = 1000000;
        scanf("%d", &N);

        for (int i=0;i<N;i++) {
            scanf("%d %d", &dots[i][0], &dots[i][1]);
            x += dots[i][0];
            y += dots[i][1];
        }

        dfs(0, 0);
        printf("%.10lf\n", result);
    }

    return 0;
}