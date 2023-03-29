#include <stdio.h>
#include <stdlib.h>

double f1(int n){
    return n + 4.23;
}

double wywolaj(double (*funkcja2)(int) , int n){
    return funkcja2(n);
}

int main()
{
    int n = 5;
    double (*wskF1)(int) = &f1;
    printf("%f", wywolaj(wskF1,n));
}
