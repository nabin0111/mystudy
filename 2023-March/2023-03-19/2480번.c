#include <stdio.h>

int main() {
    int num[3];
    int tmp, idx;

    scanf("%d %d %d", &num[0], &num[1], &num[2]);

    for (int i=1;i<3;i++) {
        tmp = num[i];
        idx = i;
        for (int j=i-1;j>=0;j--) {
            if (num[j] > tmp) {
                num[j+1] = num[j];
                idx = j;
            } else {
                break;
            }
        }
        num[idx] = tmp;
    }

    if (num[0] == num[2]) {
        printf("%d", 10000+(1000*num[0]));
    } else if (num[0] == num[1]) {
        printf("%d", 1000+(100*num[0]));
    } else if (num[1] == num[2]) {
        printf("%d", 1000+(100*num[1]));
    } else {
        printf("%d", 100*num[2]);
    }

    return 0;
}