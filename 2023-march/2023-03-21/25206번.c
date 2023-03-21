#include <stdio.h>
#include <string.h>

float change(char* grade) {
    char a = grade[0];
    float result = 0;
    
    if (a == 'A') {
        result += 4;
    } else if (a == 'B') {
        result += 3;
    } else if (a == 'C') {
        result += 2;
    } else if (a == 'D') {
        result += 1;
    } else if (a == 'P') {
        result = -1;
    }

    if (strlen(grade) == 2 && grade[1] == '+') {
        result += 0.5;
    }

    return result;
}

int main() {
    char course[50], grade[3];
    float credit, score;
    float total_c = 0, total = 0;

    for (int i=0;i<20;i++) {
        scanf("%s %f %s", course, &credit, grade);
        score = change(grade);
        if (score == -1) {
            continue;
        }
        total_c += credit;
        total += (credit * score);
    }

    printf("%f", total / total_c);

    return 0;
}