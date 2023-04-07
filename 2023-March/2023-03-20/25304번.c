#include <stdio.h>

int main() {
    long X, total = 0;
    int N, a, b;

    scanf("%ld", &X);
    scanf("%d", &N);

    while (N--) {
        scanf("%d %d", &a, &b);
        total += (a * b);
    }

    if (X == total) {
        printf("Yes");
    } else {
        printf("No");
    }
    
    return 0;
}