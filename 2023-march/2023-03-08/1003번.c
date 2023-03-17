#include <stdio.h>

// idea 자체는 쉽게 떠올릴 수 있었다.
// 단, 피보나치 수열을 배열로 저장하는 쉬운 방법을
// 바로 고안해내지 못해 어려움을 겪었다.
// 시간초과를 해결하는 가장 쉬운 방법은 규칙을 가지는 값들을 저장하는 것!


int main() {
    int T, N;
    int fibo[41] = {0, 1};

    for (int i=2;i<41;i++) {
        fibo[i] = fibo[i-1] + fibo[i-2];
    }

    scanf("%d", &T);

    for (int i=0;i<T;i++) {
        scanf("%d", &N);
        if (N==0) {
            printf("1");
        } else {
            printf("%d", fibo[N-1]);
        }
        printf(" %d\n", fibo[N]);
    }

    return 0;
}