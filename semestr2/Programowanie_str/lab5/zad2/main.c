#include <stdio.h>
#include <stdlib.h>

int f1(int k){
    return k+k;
}

int f2(int k){
    return k*k;
}

int wywolaj(int (*f1)(int), int (*f2)(int), int n){
    return (*f1)(n) + (*f2)(n);
}

int main()
{
    int n = 2;
    int (*wskF1)(int) = &f1;
    int (*wskF2)(int) = &f2;
    printf("Dla n = %i: %i", n,  wywolaj(wskF1, wskF2, n));
    n = 45;
    printf("\nDla n = %i: %i", n,  wywolaj(wskF1, wskF2, n));
}
