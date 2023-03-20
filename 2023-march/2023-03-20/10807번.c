#include <stdio.h>

// 배열 길이 중요하게 생각할 것

int main() {
    int N, v;
    int count[201] = {0,};
    
    scanf("%d", &N);

    while (N--) {
        scanf("%d", &v);
        count[v+100]++;
    }

    scanf("%d", &v);
    printf("%d", count[v+100]);

    return 0;
}