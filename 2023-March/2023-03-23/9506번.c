#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, sum;
    int div[100000];
    int idx = 0;

    while (1) {
        idx = 0;
        scanf("%d", &n);
        if (n == -1) {
            break;
        }

        sum = 1;
        for (int i=2;i<n;i++) {
            if (n % i == 0) {
                sum += i;
                div[idx++] = i;
            }
        }

        if (n == sum) {
            printf("%d = 1", n);
            for (int i=0;i<idx;i++) {
                printf(" + %d", div[i]);
            }
            printf("\n");
        } else {
            printf("%d is NOT perfect.\n", n);
        }
    }

    return 0;
}