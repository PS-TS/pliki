#include <stdio.h>
#include <stdlib.h>

int** funckja(int n);

int main() {
    int n = 5;

    int** arr = funckja(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}

int** funckja(int n) {
    int** arr = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        arr[i] = (int*)malloc((i + 1) * sizeof(int));
        for (int j = 0; j <= i; j++) {
            arr[i][j] = i + j;
        }
    }
    return arr;
}
