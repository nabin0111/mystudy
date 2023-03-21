#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int len, cur = 0;

    scanf("%s", str);
    len = strlen(str);

    while (cur < len-1-cur) {
        if (str[cur] != str[len-1-cur]) {
            printf("0");
            return 0;
        }
        cur++;
    }
    printf("1");

    return 0;
}