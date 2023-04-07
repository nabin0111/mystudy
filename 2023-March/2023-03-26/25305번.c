#include <stdio.h>

int main() {
    int N, k;
    int score[1000];
    int cur, idx;

    scanf("%d %d", &N, &k);

    for (int i=0;i<N;i++) {
        scanf("%d", &score[i]);
    }

    for (int i=1;i<N;i++) {
        cur = score[i];
        idx = i;
        for (int j=i-1;j>=0;j--) {
            if (score[j] < cur) {
                score[j+1] = score[j];
                idx = j;
            } else {
                break;
            }
        }
        score[idx] = cur;
    }

    printf("%d", score[k-1]);

    return 0;
}