#include <stdio.h>
#include <stdlib.h>

int funkcja(){
    int n;
    return malloc(sizeof(int));
}

int main()
{
    printf("%p", funkcja());
}
