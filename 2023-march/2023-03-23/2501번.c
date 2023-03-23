#include <stdio.h>

int main() {
    int N, K;
    int cnt = 0;

    scanf("%d %d", &N, &K);

    for (int i=1;i<=N;i++) {
        if (N % i == 0) {
            cnt++;
        }

        if (K == cnt) {
            printf("%d", i);
            return 0;
        }
    }

    printf("0");

    return 0;
}