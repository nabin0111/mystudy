#include <stdio.h>

// 유클리드 호제법

int gcd(int a, int b) {
    if (a % b == 0) {
        return b;
    } else {
        return gcd(b, a % b);
    }
}

int main() {
    long long A, B;

    scanf("%lld %lld", &A, &B);

    if (A > B) {
        printf("%lld", A * B / gcd(A, B));
    } else {
        printf("%lld", B * A / gcd(B, A));
    }

    return 0;
}