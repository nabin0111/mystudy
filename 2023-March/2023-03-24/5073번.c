#include <stdio.h>

int main() {
    int a, b, c, max;

    while (1) {
        scanf("%d %d %d", &a, &b, &c);
        if (a == 0) {
            break;
        }

        max = a;
        if (b > max) {
            max = b;
        }
        if (c > max) {
            max = c;
        }

        if (a == b && b ==c && c == a) {
            printf("Equilateral\n");
        } else if (a + b + c - max <= max) {
            printf("Invalid\n");
        } else if (a == b || b == c || c == a) {
            printf("Isosceles\n");
        } else {
            printf("Scalene\n");
        }
    }
    
    return 0;
}