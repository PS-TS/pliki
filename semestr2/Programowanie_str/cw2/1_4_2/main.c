#include <stdio.h>
#include <stdlib.h>

int main()
{
    int m, n, wynik = 1;
    printf("Wprowadz m: ");
    scanf("%i", &m);
    printf("Wprowadz n: ");
    scanf("%i", &n);

    if(m<=0 || n<=0){
        printf("m lub n nie sa dodatnie. Wprowadz liczby jeszcze raz: ");
        scanf("%i %i", &m, &n);
    }

    for(int i=0; i<m; i++){
        wynik = wynik * n;
        printf("Wielokrotnosc %i: %i \n", i+1, wynik);
    }
}
