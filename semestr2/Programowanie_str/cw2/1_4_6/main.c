#include <stdio.h>
#include <stdlib.h>

int main()
{
    int wynik = 1, n;
    printf("Podaj liczbe n: ");
    scanf("%i", &n);
    if(n<=2){
        printf("Podaj n jeszcze raz: ");
        scanf("%i", &n);
    }
    if(n%2==0){
        for(int i=2; i<=n; i++){
            if(i%2==0){
                wynik = wynik * i;
            }
        }
    } else{
        for(int i=2; i<n; i++){
            if(i%2==0){
                wynik = wynik * i;
            }
        }
    }
    printf("%i", wynik);

    return 0;
}
