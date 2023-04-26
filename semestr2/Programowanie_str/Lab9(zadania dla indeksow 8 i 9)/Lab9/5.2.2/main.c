#include <stdio.h>
#include <string.h>

int dlugosc(char napis[]) {
    int i = 0;
    while(napis[i] != '\0') {
        i++;
    }
    return i;
}

int main() {
    char napis[] = "Napis Testowy";
    int wynik = dlugosc(napis);
    printf("Dlugosc napisu '%s' to %d\n", napis, wynik);
    return 0;
}





