#include <stdio.h>

// c-a1 >= 0인 조건 잘 고려하기

int main() {
    int a1, a0, c, n0;
    
    scanf("%d %d", &a1, &a0);
    scanf("%d %d", &c, &n0);

    if ((c*n0 >= a0 + a1 * n0) && c - a1 >= 0) {
        printf("1");
    } else {
        printf("0");
    }
    
    return 0;
}