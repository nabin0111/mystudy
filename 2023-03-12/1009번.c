#include <stdio.h>
#include <math.h>

int T, a, b, result;

int main() {
    scanf("%d", &T);

    while (T--) {
        scanf("%d %d", &a, &b);
        a %= 10;
        b %= 4;

        if (b == 0) {
            b = 4;
        }
        
        result = pow(a, b);
        result %= 10;

        if (result) {
            printf("%d\n", result);
        } else {
            printf("10\n");
        }
    }

    return 0;
}