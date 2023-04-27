#include <stdio.h>
#include <stdlib.h>

void zero(int **arr, int n, int m) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            arr[i][j] = 0;
        }
    }
}

int main() {
    int n, m;
    printf("Podaj wymiary tablicy: ");
    scanf("%d %d", &n, &m);

    int **arr = malloc(n * sizeof(int *));
    for(int i = 0; i < n; i++) {
        arr[i] = malloc(m * sizeof(int));
    }

    zero(arr, n, m);

    printf("Tablica wypelniona zerami:\n");
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for(int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}
