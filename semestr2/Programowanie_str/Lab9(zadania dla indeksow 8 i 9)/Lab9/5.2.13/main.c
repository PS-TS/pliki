#include <stdio.h>
#include <string.h>

void wytnijtm(char *nap1, char *nap2) {
    int i, j;
    int len = strlen(nap1);

    for (i = 0, j = 0; i < len; i++) {
        if (nap1[i] != nap2[i]) {
            nap1[j++] = nap1[i];
        }
    }

    nap1[j] = '\0';
}

int main() {
    char nap1[] = "abcdefg";
    char nap2[] = "abdegfg";

    printf("nap1 przed: %s\n", nap1);
    wytnijtm(nap1, nap2);
    printf("nap1 po: %s\n", nap1);

    return 0;
}
