#include <stdio.h>
#include <string.h>

int main() {
    int T;
    char S[1000];

    scanf("%d", &T);

    while (T--) {
        scanf("%s", S);
        printf("%c%c\n",S[0],S[strlen(S)-1]);
    }  

    return 0;
}