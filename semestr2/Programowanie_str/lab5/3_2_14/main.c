#include <stdio.h>
#include <stdlib.h>

int wywolaj(int (*wskF1)(int), int (*wskF2)(int), unsigned int n){
    int zmienna = 0;
    for(int i = 0; i<=n; i++){
        if((*wskF1)(i) == (*wskF2)(i)){
            zmienna = 1;
        }
    }
    return zmienna;
}

int f1(int x){
    return x;
}

int f2(int x){
    return x;
}

int main()
{
    unsigned int n = 7;
    int (*wskF1)(int) = &f1;
    int (*wskF2)(int) = &f2;
    printf("%i", wywolaj(wskF1, wskF2, n));
}
