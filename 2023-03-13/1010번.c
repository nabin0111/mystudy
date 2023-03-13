#include <stdio.h>

int main() {
    int T, N, M;
    long long result;
    int a;

    scanf("%d", &T);

    while (T--) {
        result = 1;
        scanf("%d %d", &N, &M);

        if (N == M) {
            printf("%d\n", 1);
            continue;
        }
        
        if (M-N < N) {
            a = M - N;
        } else {
            a = N;
        }

        for (int i=M;i>=M-a+1;i--) {
            result *= i;
        }
        
        for (int i=a;i>1;i--) {
            result /= i;
        }

        printf("%lld\n", result);
    }

    return 0;
}