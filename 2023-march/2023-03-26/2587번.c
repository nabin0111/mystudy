#include <stdio.h>

int main() {
    int num[5];
    int cur, idx;

    for (int i=0;i<5;i++) {
        scanf("%d", &num[i]);
        
    }

    for (int i=1;i<5;i++) {
        cur = num[i];
        idx = i;
        for (int j=i-1;j>=0;j--) {
            if (num[j] > cur) {
                num[j+1] = num[j];
                idx = j;
            } else {
                break;
            }
        }
        num[idx] = cur;
    }

    printf("%d\n", (num[0]+num[1]+num[2]+num[3]+num[4])/5);
    printf("%d", num[2]);
    
    return 0;
}