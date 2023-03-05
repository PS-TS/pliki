#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, wynik=1;
    printf("Podaj liczbe n: ");
    scanf("%i", &n);
    for(int i=n; i>=1; i--){
        wynik = wynik * i;
    }
    printf("%i", wynik);
}
