#include <stdio.h>
#include <math.h>
#include <memory.h>

int main() {
    long long min, max, tmp, sqaure;
    long long start, cnt = 0;

    scanf("%lld %lld", &min, &max);
    char num[max-min+1];
    memset(num, 0, sizeof(num));
    
    for (long i=2;i<=sqrt(max);i++) {
        sqaure = i * i;        
        start = max / sqaure;
        tmp = start * sqaure;
        while (tmp >= min) {
            if (num[tmp-min] == 0) {
                num[tmp-min] = 1;
                cnt++;
            }
            tmp -= sqaure;
        }    
        if (cnt == max-min+1) {
            break;
        }    
    }

    long long result = 0;
    for (long long i=0;i<max-min+1;i++) {
        if (num[i]) {
            result++;
        }
    }

    printf("%lld", max-min+1-result);

    return 0;
}