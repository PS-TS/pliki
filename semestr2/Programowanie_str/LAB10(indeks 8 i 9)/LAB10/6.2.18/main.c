#include <stdio.h>
#include <stdlib.h>

void w(int tab[][3], int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int tablica[2][3] = {{1, 2, 3}, {4, 5, 6}};
    w(tablica, 2, 3);
    return 0;
}
