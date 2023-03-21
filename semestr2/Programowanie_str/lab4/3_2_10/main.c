#include <stdio.h>
#include <stdlib.h>

int funkcja(){
    double n;
    int *wskaznik1 = &n;
    return wskaznik1;
}

int main()
{
    printf("%p", funkcja());
}
