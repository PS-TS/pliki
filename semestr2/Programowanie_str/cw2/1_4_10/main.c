#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, y=1, zaokr;
    printf("Wprowadz liczbe n: ");
    scanf("%i", &n);
    float temp, sqrt;

    sqrt = (float)n / 2;
    temp = 0;

    while(sqrt != temp){
        temp = sqrt;
        sqrt = ( n/temp + temp) / 2;
    }
    printf("Pierwiastek z %i wynosi %f", n, sqrt);

    zaokr = sqrt/y;
    printf("\nZaokraglony w dol: %i", zaokr);

}
