#include <stdio.h>
#include <string.h>

void przepisz(char napis1[], char napis2[]) {
    strcpy(napis2, napis1);
}

int main() {
    char napis1[] = "Napis testowy";
    char napis2[100];

    przepisz(napis1, napis2);

    printf("Napis 1: %s\n", napis1);
    printf("Napis 2: %s\n", napis2);

    return 0;
}
