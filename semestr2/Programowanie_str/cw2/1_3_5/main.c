#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int opcja;
    printf("Z jakich danych obliczyc pole?\n1 - podstawa i wysokosc\n2 - wszystkie boki trojkata\nOpcja: ");
    scanf("%i", &opcja);

    if(opcja==1){
            float a, h, pole;
        printf("Podaj dlugosc podstawy: ");
        scanf("%f", &a);
        printf("Podaj dlugosc wysokosci: ");
        scanf("%f", &h);
        pole = ((a*h)/2);
        printf("Pole rowna sie: %f", pole);
    } else if(opcja==2){
        float a, b, c, pole, p;
        printf("Podaj dlugosc boku a: ");
        scanf("%f", &a);
        printf("Podaj dlugosc boku b: ");
        scanf("%f", &b);
        printf("Podaj dlugosc boku c: ");
        scanf("%f", &c);

        p = (a+b+c)/2.0;
        pole = sqrt(p*(p-a)*(p-b)*(p-c));
        printf("Pole rowna sie: %f", pole);
    }


}
