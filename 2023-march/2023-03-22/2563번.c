#include <stdio.h>

int main() {
    int rect[100][100] = {0,};
    int n, l, b, result = 0;

    scanf("%d", &n);

    while (n--) {
        scanf("%d %d", &l, &b);

        for (int i=l;i<l+10;i++) {
            for (int j=b;j<b+10;j++) {
                if (rect[j][i] == 0) {
                    rect[j][i] = 1;
                    result++;
                }
            }
        }
    }

    printf("%d", result);

    return 0;
}