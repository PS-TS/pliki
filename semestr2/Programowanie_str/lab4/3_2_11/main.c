#include <stdio.h>
#include <stdlib.h>

int funkcja(int n){
    return malloc(n*sizeof(int));
}

int main()
{
    int n = 7;
    printf("%p", funkcja(n));
}
