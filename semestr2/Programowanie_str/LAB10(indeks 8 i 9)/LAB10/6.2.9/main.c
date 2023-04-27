#include <stdio.h>
#include <stdlib.h>

void zera(int** arr, int n, int m){
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            arr[i][j] = 0;
        }
    }
}

int main(){
    int n = 3;
    int m = 4;

    int** arr = (int**) malloc(n * sizeof(int*));
    for(int i=0; i<n; i++){
        arr[i] = (int*) malloc(m * sizeof(int));
    }

    zera(arr, n, m);

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for(int i=0; i<n; i++){
        free(arr[i]);
    }
    free(arr);

    return 0;
}
