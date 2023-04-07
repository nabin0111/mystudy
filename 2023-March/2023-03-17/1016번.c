#include <stdio.h>
#include <math.h>
#include <memory.h>

// 미해결

int main() {
    long long min, max, tmp, sqaure;

    scanf("%lld %lld", &min, &max);
    char num[max-min+1];
    memset(num, 0, sizeof(num));
    
    for (long i=2;i<=sqrt(max);i++) {
        sqaure = i * i;
        tmp = sqaure;
        for (long j=1;j<=max/sqaure;j++) {
            printf("tmp: %lld\n", tmp);
            num[tmp-min] = 1;
            tmp += sqaure;
        }
    }

    long long result = 0;
    for (long long i=0;i<max-min+1;i++) {
        if (num[i]) {
            result++;
        }
    }

    printf("%lld", max-min+1-result);
    scanf("%lld", &min);

    return 0;
}