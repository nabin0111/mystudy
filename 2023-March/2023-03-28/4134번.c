#include <stdio.h>
#include <math.h>

// 변수 동일하게 맞출 것
// 원리 제대로 이해하고 작성할 것

int isPrime(long long x) {
    long long lim = sqrt(x);
    if (x < 2) {
        return 0;
    }
    for (long long i=2;i<lim+1;i++) {
        if (x % i == 0){
            return 0;
        }
    }
    return 1;
}

int main() {
    long long T, n;

    scanf("%lld", &T);
    while (T--) {
        scanf("%lld", &n);
        while (isPrime(n++) == 0);
        printf("%lld\n", n-1);
    }

    return 0;
}