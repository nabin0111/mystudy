#include <stdio.h>
#include <string.h>

// 다른 분 풀이 참고해서 수정

int main() {
    char board[5][15];

    memset(board, '*', sizeof(board));

    for (int i=0;i<5;i++) {
        scanf("%s", board[i]);   
    }

    for (int i=0;i<15;i++) {
        for (int j=0;j<5;j++) {
            if (board[j][i] != '*' && board[j][i] != '\0') {
                printf("%c", board[j][i]);
            }
        }
    }

    return 0;
}