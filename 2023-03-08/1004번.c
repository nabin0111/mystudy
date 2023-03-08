#include <stdio.h>

int main() {
    int T, N;
    int x1, y1, x2, y2;
    int result, tmp;
    int cx, cy, r;

    scanf("%d", &T);

    for (int i=0;i<T;i++) {
        result = 0;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        scanf("%d", &N);
        for (int j=0;j<N;j++) {
            tmp = 0;
            scanf("%d %d %d", &cx, &cy, &r);
            if ((cx-x1)*(cx-x1) + (cy-y1)*(cy-y1) < r*r) {
                tmp++;
            }
            if ((cx-x2)*(cx-x2) + (cy-y2)*(cy-y2) < r*r) {
                tmp++;
            }

            if (tmp == 1) {
                result++;
            }
        }
        printf("%d\n", result);
    }

    return 0;
}