#include <stdio.h>

int main() {
    int N, M;
    int basket[101] = {0,};
    int i, j ,k;

    scanf("%d %d", &N, &M);

    while (M--) {
        scanf("%d %d %d", &i, &j, &k);
        for (;i<=j;i++) {
            basket[i] = k;
        }
    }

    for(i=1;i<=N;i++) {
        printf("%d ", basket[i]);
    }

    return 0;
}