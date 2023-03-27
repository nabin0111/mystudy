#include <stdio.h>

int gcd(int a, int b) {
    if (a % b == 0) {
        return b;
    } else {
        return gcd(b, a % b);
    }
}

int main() {
    int A, B, C, D, g;

    scanf("%d %d %d %d", &A, &B, &C, &D);
    
    if (B == D) {
        if (A+C > B) {
            g = gcd(A+C, B);
        } else {
            g = gcd(B, A+C);
        }
        printf("%d %d", (A+C)/g, B/g);
    } else {
        A = A*D + B*C;
        if (A > B*D) {
            g = gcd(A, B*D);
        } else {
            g = gcd(B*D, A);
        }
        printf("%d %d", A/g, B*D/g);
    }

    return 0;
}