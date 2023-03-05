#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int a,b,c;
    float delta;
    printf("Wprowadz a: ");
    scanf("%i", &a);
    printf("Wprowadz b: ");
    scanf("%i", &b);
    printf("Wprowadz c: ");
    scanf("%i", &c);

    delta = (b*b)-(4*a*c);
    printf("Delta = %f", delta);
    if(delta>0){
        float x1, x2;
        x1 = (-b - sqrt(delta))/(2*a);
        x2 = (-b + sqrt(delta))/(2*a);
        printf("\n%f", x1);
        printf("\n%f", x2);
    } else if(delta==0){
        float x = (-b)/(2*a);
        printf("\n%f", x);
    } else{
        printf("\nBrak rozwiazan");
    }
}
