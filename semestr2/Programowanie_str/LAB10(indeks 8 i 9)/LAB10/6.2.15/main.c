#include <stdio.h>
#include <stdlib.h>

int w(int n, int arr[n][100][100]) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 100; j++) {
            for (int k = 0; k < 100; k++) {
                sum += arr[i][j][k];
            }
        }
    }
    return sum;
}

int main() {
    int n = 2;
    int arr[2][100][100];

    // wype³nienie tablicy losowymi wartoœciami
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 100; j++) {
            for (int k = 0; k < 100; k++) {
                arr[i][j][k] = rand() % 10; // losowa wartoœæ od 0 do 9
            }
        }
    }

    int result = w(n, arr);
    printf("Suma elementow tablicy: %d\n", result);

    return 0;
}
