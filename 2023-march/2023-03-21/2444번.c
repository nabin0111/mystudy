#include <stdio.h>

// * 뒤에는 스페이스를 사용할 필요가 X

int main() {
    int space, star=1, step=1;
    int N;

    scanf("%d", &N);
    space = N - 1;

    for (int i=1;i<2*N;i++) {
        if (!space) {
            step = -1;
        }
        for (int j=0;j<space;j++) {
            printf(" ");
        }
        for (int j=0;j<star;j++) {
            printf("*");
        }
        printf("\n");
        space -= step;
        star += 2 * step;
    }

    return 0;
}