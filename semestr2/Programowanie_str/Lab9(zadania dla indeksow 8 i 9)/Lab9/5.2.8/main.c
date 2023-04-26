#include <stdio.h>
#include <ctype.h>

void DuzeLitery(char *str) {
    int i = 0;
    while (str[i]) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = toupper(str[i]);
        }
        i++;
    }
}

int main() {
    char str[100];

    printf("Podaj napis: ");
    fgets(str, 100, stdin);

    DuzeLitery(str);

    printf("Napis po zamianie na duze litery: %s", str);

    return 0;
}
