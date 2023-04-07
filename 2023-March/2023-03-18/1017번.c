#include <stdio.h>
#include <math.h>
#include <string.h>

// 이분 매칭 아이디어: 홀수 + 짝수
// DFS에 익숙해지고 다시 풀어볼 것

int N;
int answer[50] = {0,};

int isPrime(int a) {
    for (int i=3;i<=sqrt(a);i++) {
        if (a % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int odd[50] = {0,};
    int even[50] = {0,};
    int o = 0, e = 0, tmp;

    scanf("%d", &N);

    for (int i=0;i<N;i++) {
        scanf("%d", &tmp);
        if (tmp % 2) {
            odd[o++] = tmp;
        } else {
            even[e++] = tmp;
        }
    }

    if (strlen(odd) != N/2) {
        printf("-1");
        return 0;
    }

    return 0;
}