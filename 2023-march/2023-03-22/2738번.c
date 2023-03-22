#include <stdio.h>

int main() {
    int A[100][100];
    int N, M, input;

    scanf("%d %d", &N, &M);

    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            scanf("%d", &input);
            A[i][j] += input;
        }
    }

    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }

    return 0;
}