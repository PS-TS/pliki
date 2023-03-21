#include <stdio.h>
#include <stdlib.h>

void funkcja(int n, int *w){
    *w = n;
}

int main()
{
    int n = 5, x = 1;
    int *w = &x;
    printf("%i", x);
    funkcja(n, w);
    printf("\n%i", x);
}
