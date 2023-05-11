#include <stdio.h>
#include <stdlib.h>

struct Osoba {
	char Imie[20];
	int Wiek;
};

struct Osoba initOsoba() {
	struct Osoba A;

	printf("Podaj imie osoby: ");
	scanf_s("%s", A.Imie, sizeof(A.Imie));
	printf("\nPodaj wiek osoby: ");
	scanf_s("%d", &A.Wiek);

	return A;
}

void pokazOsoba(struct Osoba human) {
	printf("Imie: %s\nWiek: %d", human.Imie, human.Wiek);
}

void urodziny(struct Osoba* czlowiek) {
	czlowiek->Wiek++;
}

int main() {
	struct Osoba Os1 = { "Adam", 22 };
	struct Osoba Os2 = initOsoba();
	pokazOsoba(Os1);
	urodziny(&Os2);
	pokazOsoba(Os2);
}