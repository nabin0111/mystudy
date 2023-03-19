#include <stdio.h>

int main() {
    int A, B, C;
    int hour, min;

    scanf("%d %d", &A, &B);
    scanf("%d", &C);

    min = (B + C);
    hour = (A + (min / 60)) % 24;
    min %= 60;

    printf("%d %d", hour, min);

    return 0;
}