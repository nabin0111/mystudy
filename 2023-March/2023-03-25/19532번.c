#include <stdio.h>

int main() {
    int a, b, c, d, e, f;
    int i, j, x, y;

    scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
    i = b*d - e*a;
    j = c*d - f*a;

    if (i == 0) {
        y = c / (a + b);
    } else {
        y = j / i;
    }
    
    if (a == 0) {
        x = (f - e * y) / d;
    } else {
        x = (c - b * y) / a;
    }

    printf("%d %d", x, y);

    return 0;
}