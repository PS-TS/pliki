#include <stdio.h>
#include <stdlib.h>

void funkcja(int *x, int *y){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int x = 5, y = 9;
    funkcja(&x, &y);
    printf("%i", x);
    printf("\n%i", y);
}
