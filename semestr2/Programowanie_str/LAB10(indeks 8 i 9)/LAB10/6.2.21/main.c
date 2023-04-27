#include <stdio.h>
#include <stdlib.h>

void w(int tab[][5], int n, int m) {
    int temp;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m / 2; j++) {
            temp = tab[i][j];
            tab[i][j] = tab[i][m - 1 - j];
            tab[i][m - 1 - j] = temp;
        }
    }
}

int main() {
    int tab[3][5] = {
        {1, 2, 3, 4, 5},
        {6, 7, 8, 9, 10},
        {11, 12, 13, 14, 15}
    };

    printf("Przed odwroceniem:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }

    w(tab, 3, 5);

    printf("Po odwroceniu:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }

    return 0;
}
