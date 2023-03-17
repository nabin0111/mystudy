#include <stdio.h>
#include <string.h>
// 정규표현식으로 풀면 더 쉬울 듯

int T;
char string[200];

int first(int s) {
    if (string[++s] != '0' || string[++s] != '0') {
        return 0;
    }

    while ((++s) != strlen(string) && string[s] == '0');
    if (s == strlen(string)) {
        return 0;
    }

    while ((s++) != strlen(string) && string[s] == '1');
    if (s == strlen(string)) {
        return -1;
    }
    if (s + 1 > strlen(string) - 1) {
        return 0;
    }

    if (string[s+1] == '0') {
        if (string[s-2] == '1') {
            return s-1;
        }
        return 0;
    } else {
        return s;
    }
}

int second(int s) {
    if (string[++s] == '1') {
        if (s == strlen(string) - 1) {
            return -1;
        }
        return ++s;
    }
    return 0;
}

int main() {
    int s;

    scanf("%d", &T);

    while (T--) {
        s = 0;
        scanf("%s", string);

        do {
            if (string[s] == '1') {
                s = first(s);
            } else {
                s = second(s);
            }
        } while (s != 0 && s != -1);

        if (s == -1) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }

    return 0;
}