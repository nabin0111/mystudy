#include <stdio.h>

int main() {
    int origin[6] = {1, 1, 2, 2, 2, 8};
    int real[6];

    for (int i=0;i<6;i++) {
        scanf("%d", &real[i]);
    }

    for (int i=0;i<6;i++) {
        printf("%d ", origin[i]-real[i]);
    }

    return 0;
}