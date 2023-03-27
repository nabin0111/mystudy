#include <stdio.h>

// 최소공배수 = a * b / 최대공약수
// 유클리드 호제법

int gcd(int a, int b) {
    if (a % b == 0) {
        return b;
    } else {
        return gcd(b, a % b);
    }
}

int main() {
    int T, A, B;

    scanf("%d", &T);

    while (T--) {
        scanf("%d %d", &A, &B);
        if (A > B) {
            printf("%d\n", A * B / gcd(A, B));
        } else {
            printf("%d\n", B * A / gcd(B, A));
        }
    }

    return 0;
}