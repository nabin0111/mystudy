#include <stdio.h>
#include <memory.h>

// 맞긴 했는데 다른 사람의 예제 코드와 비교하면 좋을 듯

int T, M, N, K;
int map[50][50];
int visited[50][50];
int result;

void check(int a, int t) {
    int r = a / N, c = a % N;

    if (!map[r][c] || !K) {
        return;
    }
    if (!visited[r][c]) {
        visited[r][c] = 1;
        K--;
    } else {
        return;
    }
    if (!t) {
        result++;
    }
    
    if (r) {
        check(a-N, 1);
    }
    if (c) {
        check(a-1, 1);
    }
    if (r != M-1) {
        check(a+N, 1);
    }
    if (c != N-1) {
        check(a+1, 1);
    }
}

int main() {
    int X, Y;

    scanf("%d", &T);

    while (T--) {
        memset(map, 0, sizeof(map));
        memset(visited, 0, sizeof(visited));
        result = 0;
        scanf("%d %d %d", &M, &N, &K);

        for (int i=0;i<K;i++) {
            scanf("%d %d", &X, &Y);
            map[X][Y] = 1;
        }

        for (int i=0;i<M*N;i++) {
            if (!K) {
                break;
            }

            if (map[i/N][i%N]) {
                check(i, 0);
            }
        }        
        
        printf("%d\n", result);
    }

    return 0;
}