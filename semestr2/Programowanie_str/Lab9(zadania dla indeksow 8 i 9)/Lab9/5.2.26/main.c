#include <stdio.h>
#include <ctype.h>
#include <string.h>

void funkcja(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        if (islower(str[i])) {
            str[i] = toupper(str[i]);
        }
    }
}

int main() {
    char str[] = "test, Test, tEst";
    printf("Przed: %s\n", str);
    funkcja(str);
    printf("Po: %s\n", str);
    return 0;
}
