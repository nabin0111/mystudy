#include <stdio.h>

int main() {
    int N, M, i, j, tmp;
    int basket[101];

    scanf("%d %d", &N, &M);

    for (i=1;i<=N;i++) {
        basket[i] = i;
    }

    while (M--) {
        scanf("%d %d", &i, &j);
        while (i <= j) {
            tmp = basket[i];
            basket[i++] = basket[j];
            basket[j--] = tmp;
        }
    }

    for (i=1;i<=N;i++) {
        printf("%d ", basket[i]);
    }

    return 0;
}