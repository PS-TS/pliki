#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

int main()
{
    int a, b, c, d;
    printf("Wprowadz a: ");
    scanf("%i", &a);
    printf("Wprowadz b: ");
    scanf("%i", &b);
    printf("Wprowadz c: ");
    scanf("%i", &c);
    printf("Wprowadz d: ");
    scanf("%i", &d);

    int x = 0;
    while(abs(a)*pow(x,2) + b*x + c <= d){
        x++;
    }
    printf("A) %d\n", x);
    x=0;

    while(5*pow(x,2) + a*x + b < c){
        x++;
    }
    printf("B) %d\n", x-1);
    x=0;

    while(5*pow(x,2) + a*x + b <= c){
        x++;
    }
    printf("C) %d\n", x-1);
}
