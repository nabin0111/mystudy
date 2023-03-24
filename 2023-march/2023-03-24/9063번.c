#include <stdio.h>

int main() {
    int l, r, t, b;
    int N, x, y;

    scanf("%d", &N);
    scanf("%d %d", &x, &y);
    l = x;
    r = x;
    t = y;
    b = y;

    N--;
    while (N--) {
        scanf("%d %d", &x, &y);
        if (x < l) {
            l = x;
        } else if (x > r) {
            r = x;
        }

        if (y > t) {
            t = y;
        } else if (y < b) {
            b = y;
        }
    }

    printf("%d", (r-l) * (t-b));

    return 0;
}