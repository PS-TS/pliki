#include <stdio.h>
#include <stdlib.h>

int funkcja(int *x, int *y){
    if(*x > *y)
        return *x;
    else
        return *y;
}

int main()
{
    int x = 5, y = 2;
    int *wskaznik1 = &x;
    int *wskaznik2 = &y;
    printf("%i", funkcja(wskaznik1, wskaznik2));
}
