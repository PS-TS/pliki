#include <stdio.h>
#include <stdlib.h>

void funkcja(int *x, int *y){
    if(*y < *x){
        int temp;
        temp = *x;
        *x = *y;
        *y = temp;
    }
}

int main()
{
    int x = 9, y = 5;
    funkcja(&x, &y);
    printf("%i", x);
    printf("\n%i", y);
}
