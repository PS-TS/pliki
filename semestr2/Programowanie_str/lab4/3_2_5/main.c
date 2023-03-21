#include <stdio.h>
#include <stdlib.h>

int funkcja(int *x, int *y){
    int suma = *x + *y;
    return suma;
}

int main()
{
    int const x = 5, y = 9;
    printf("%i", funkcja(&x, &y));
}
