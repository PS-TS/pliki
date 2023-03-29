#include <stdio.h>
#include <stdlib.h>

int wywolaj(int n){
    if(n == 0 || n == 1){
        return 1;
    }
    else if(n%3 == 0 && n>0){
        return wywolaj(n/3);
    } else if(n%3 == 1 && n>0){
        return wywolaj(n/3)+1;
    } else if(n%3 == 2 && n>=0){
        return wywolaj(n-1)-1;
    }
}

int main()
{
    printf("%i", wywolaj(5));
    printf("\n%i", wywolaj(901));
}
