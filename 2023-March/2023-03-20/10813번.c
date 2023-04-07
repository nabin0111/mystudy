#include <stdio.h>

int main() {
    int N, M;
    int basket[101];
    int i, j, tmp;

    scanf("%d %d", &N, &M);

    for (i=1;i<=N;i++) {
        basket[i] = i;
    }

    while (M--) {
        scanf("%d %d", &i, &j);
        tmp = basket[i];
        basket[i] = basket[j];
        basket[j] = tmp;
    }

    for (int i=1;i<=N;i++) {
        printf("%d ", basket[i]);
    }

    return 0;
}