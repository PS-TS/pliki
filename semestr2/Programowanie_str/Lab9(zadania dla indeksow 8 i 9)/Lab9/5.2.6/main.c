#include <stdio.h>
#include <string.h>

void kopiujn(char nap1[], char nap2[], int n) {
    int len1 = strlen(nap1);
    int i;

    for (i = 0; i < n && i < len1; i++) {
        nap2[i] = nap1[i];
    }

    if (i <= n) {
        nap2[i] = 0;
    }
}

int main() {
    char nap1[] = "Ala ma kota";
    char nap2[20];

    kopiujn(nap1, nap2, 7);

    printf("nap1: %s\n", nap1);
    printf("nap2: %s\n", nap2);

    return 0;
}
