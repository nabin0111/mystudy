#include <stdio.h>

int main() {
    int a, b, c;
    int cnt;

    scanf("%d %d %d", &a, &b, &c);

    if (a == 60 && b == 60 & c == 60) {
        printf("Equilateral");
    } else if (a + b + c != 180) {
        printf("Error");
    } else if (a == b || b == c || c == a) {
        printf("Isosceles");
    } else {
        printf("Scalene");
    }

    return 0;
}