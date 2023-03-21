#include <stdio.h>
#include <stdlib.h>

void funkcja(int const *x, int *y){
    *y = *x;
}

int main()
{
    int const x = 2;
    int y = 7;
    funkcja(&x, &y);
    printf("%i", x);
    printf("\n%i", y);
}
