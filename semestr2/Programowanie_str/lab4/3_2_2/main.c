#include <stdio.h>
#include <stdlib.h>

int* funkcja(int *x, int *y){
    if(*x>*y)
        return x;
    else
        return y;
}

int main()
{
    int x = 4, y = 7;
    int *wskaznik1 = &x;
    int *wskaznik2 = &y;

    printf("%p", funkcja(wskaznik1, wskaznik2));
}
