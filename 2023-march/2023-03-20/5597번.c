#include <stdio.h>

int main() {
    int stud[31] = {0,};
    int submit, N = 28;

    while (N--) {
        scanf("%d", &submit);
        stud[submit]++;
    }

    for (int i=1;i<31;i++) {
        if (!stud[i]) {
            printf("%d\n", i);
        }
    }

    return 0;
}