#include <stdio.h>
#include <stdlib.h>

int foo(int *x, const int *y){
    return *x - *y;
}

int main()
{
    const int x = 4;
    int y = 1;
    int *wsk1 = &x;
    const int *wsk2 = &y;
    printf("%i", foo(wsk1, wsk2));
}
