#include <stdio.h>
#include <math.h>

int main() {
    int T, x, y;
    int d, root;
    int result;

    scanf("%d", &T);

    while (T--) {
        scanf("%d %d", &x, &y);
        d = y - x;

        if (d < 4) {
            result = d;
        } else {
            root = sqrt(d);
            
            if (root * root == d) {
                result = 2 * root - 1;
            } else if (d - root <= root * root) {
                result = 2 * root;
            } else {
                result = 2 * root + 1;
            }
        }

        printf("%d\n", result);
    }

    return 0;
}