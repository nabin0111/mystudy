#include <stdio.h>
#include <math.h>
// 꽤 간단하게 규칙 찾아서 해결함 (나중에 블로그 작성하기)

int T, a, b, result;

int main() {
    scanf("%d", &T);

    while (T--) {
        scanf("%d %d", &a, &b);
        a %= 10;
        b %= 4;

        if (b == 0) {
            b = 4;
        }
        
        result = pow(a, b);
        result %= 10;

        if (result) {
            printf("%d\n", result);
        } else {
            printf("10\n");
        }
    }

    return 0;
}