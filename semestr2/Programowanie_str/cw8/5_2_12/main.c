#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
void wytnijzn(char *nap1, char *nap2) {
    int i, j, k;
    char c;
    int n1 = 0, n2 = 0;

    while (nap1[n1] != '\0') {
        n1++;
    }

    while (nap2[n2] != '\0') {
        n2++;
    }

    for (i = j = 0; i < n1; i++) {
        c = nap1[i];
        for (k = 0; k < n2; k++) {
            if (c == nap2[k]) {
                nap1[j++] = c;
                break;
            }
        }
    }
    nap1[j] = '\0';
}

int main()
{
    char nap1[]="Fajny program",nap2[]="Fajna partia";
    wytnijzn(nap1,nap2);
    printf("%s\n",nap1);
    return 0;
}
