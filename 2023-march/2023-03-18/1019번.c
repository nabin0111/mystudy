#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    char N[15];
    long long tmp = 1;
    long long count[10] = {0,};

    scanf("%s", N);
    
    if (strlen(N) == 1) {
        for (int i=1;i<=atoi(N);i++)
            count[i]++;
    } else {
        for (int i=strlen(N)-2;i>=0;i--) {
            count[N[i]] += atoi(&N[i+1]) + 1;
            printf("%d\n", count[N[i]]);
            for (int j=0;j<10;j++) {
                count[j]++;
            }
        }
    }

    for (int i=0;i<10;i++) {
        printf("%lld ", count[i]);
    }
    scanf("%d", &N);

    return 0;
}