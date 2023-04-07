#include <stdio.h>

int main() {
    int N, M;
    int i, j, k, begin;
    int basket[101], temp[101];

    scanf("%d %d", &N, &M);
    for (i=1;i<=N;i++) {
        basket[i] = i;
    }

    while (M--) {
        scanf("%d %d %d", &i, &j, &k);
        begin = i;
        for (int a=i;a<k;a++) {
            temp[a] = basket[a];
        }
        for (int a=k;a<=j;a++) {
            basket[begin++] = basket[a];
        }
        for (int a=i;a<k;a++) {
            basket[begin++] = temp[a];
        }
    }

    for (i=1;i<=N;i++) {
        printf("%d ", basket[i]);
    }

    return 0;
}