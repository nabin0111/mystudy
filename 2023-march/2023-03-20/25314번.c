#include <stdio.h>

int main() {
    int N;

    scanf("%d", &N);

    while (N) {
        printf("long ");
        N -= 4;
    }
    printf("int");

    return 0;
}