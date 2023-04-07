#include <stdio.h>

int main() {
    int max = 0, r = 1, c = 1;
    int in;

    for (int i=0;i<9;i++) {
        for (int j=0;j<9;j++) {
            scanf("%d", &in);
            if (in > max) {
                max = in;
                r = i + 1;
                c = j + 1;
            }
        }
    }

    printf("%d\n", max);
    printf("%d %d", r, c);
    
    return 0;
}