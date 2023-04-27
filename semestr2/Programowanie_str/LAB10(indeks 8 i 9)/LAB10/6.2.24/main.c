#include <stdio.h>
#include <stdlib.h>


void w(int tab[][3], int n, int m) {
    int tmp[m];
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            tmp[j] = tab[i][j];
        }
        for(int j = 0; j < m; j++) {
            tab[i][(j+1) % m] = tmp[j];
        }
    }
}

int main() {
    int n = 2, m = 3;
    int tab[n][m];

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            tab[i][j] = i*m + j;
        }
    }

    printf("Przed zmiana:\n");
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }

    w(tab, n, m);

    printf("Po zmianie:\n");
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }

    return 0;
}
