#include <stdio.h>
#include <stdlib.h>

int main()
{
    int liczba1, liczba2, dzialanie, kontynuacja=1;
    while(kontynuacja!=0){
        printf("Podaj pierwsza liczbe: ");
        scanf("%i", &liczba1);
        printf("Podaj pierwsza liczbe: ");
        scanf("%i", &liczba2);
        printf("Jaka operacje arytmetyczna chcesz wykonac? \n 1 - dodawanie, \n 2 - odejmowanie, \n 3 - mnozenie, \n 4 - dzielenie \n Wprowadz numer operacji: ");
        scanf("%i", &dzialanie);

        switch(dzialanie){
            case 1: printf("Wynik = %i \n", liczba1+liczba2);
                break;
            case 2: printf("Wynik = %i \n", liczba1-liczba2);
                break;
            case 3: printf("Wynik = %i \n", liczba1*liczba2);
                break;
            case 4: printf("Wynik = %f \n", (float)liczba1/(float)liczba2);
                break;
        }
        printf("Obliczyc jeszcze raz? 1 - tak, 0 - nie: ");
        scanf("%i", &kontynuacja);
    }
}
