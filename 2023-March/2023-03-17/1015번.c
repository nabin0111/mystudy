#include <stdio.h>

int A[50];
int order[50];
int tmp, idx;

void insert(int n) {
    for (int i=1;i<n;i++) {
        tmp = A[i];
        idx = i;
        
        for (int j=i-1;j>=0;j--) {
            if (A[j] > tmp) {
                A[j+1] = A[j];
                order[j+1] = order[j];
                idx = j;
            }
        }

        A[idx] = tmp;
        order[idx] = i;
    }
}

int main() {
    int N;

    scanf("%d", &N);

    for (int i=0;i<N;i++) {
        scanf("%d", &A[i]);
        order[i] = i;
    }

    insert(N);

    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            if (order[j] == i) {
                printf("%d ", j);
            }
        }
    }

    return 0;
}