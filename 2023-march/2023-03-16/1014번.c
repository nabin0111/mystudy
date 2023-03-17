// 원리 이해부터 안 돼서 참고했지만,, 일단 포기
// 대충 원리를 어느 정도 이해는 함
#include <stdio.h>

int main() {
    int T;

    scanf("%d", &T);

    while (T--) {
        int N, M, broken = 0;
        scanf("%d %d", &N, &M);
        int seat[10][10] = {0,};

        for (int i=0;i<N;i++) {
            getchar();
            for (int j=0;j<M;j++) {
                if (getchar() == 'x') {
                    seat[i][j] = 1;
                    broken++;
                }             
            }
        }


    }

    return 0;
}