#include <stdio.h>
#include <stdlib.h>
void kopiuj(char *napis, char *tablica) {
    int i = 0;

    while (napis[i] != '\0') {
        tablica[i] = napis[i];
        i++;
    }

    tablica[i] = '\0';
}
int main()
{
    char napis[]="Program",tablica[10];
    kopiuj(napis,tablica);
    printf("%s\n",tablica);
    return 0;
}
