#include <stdio.h>
#include <stdlib.h>

void funkcja(int** arr, int n, int m);

int main() {
    int** arr = (int**)malloc(3 * sizeof(int*));
    for (int i = 0; i < 3; i++) {
        arr[i] = (int*)malloc(4 * sizeof(int));
        for (int j = 0; j < 4; j++) {
            arr[i][j] = i + j;
        }
    }

    funkcja(arr, 3, 4);

    return 0;
}

void funkcja(int** arr, int n, int m) {
    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);
}
