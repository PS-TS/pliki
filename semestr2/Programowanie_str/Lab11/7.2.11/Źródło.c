#include <stdio.h>
#include <stdlib.h>

union Liczba {
	int cal;
	float wym;
};

struct Dane {
	int tp;
	union Liczba zaw;
};

struct Dane wczytaj() {
	union Liczba N;
	struct Dane Costam;
	int wybor;

	printf("Jakiego typu liczbe chcesz wczytac?\n1 - Calkowita\n2 - Wymierna\n");
	scanf_s("%d", &wybor);
	while (wybor < 1 && wybor  > 2) {
		printf("\nWybierz miêdzy 1 a 2\n");
		scanf_s("%d", &wybor);
	}

	Costam.tp = wybor;

	if (wybor - 1 == 0) {
		int a;
		printf("\nPodaj liczbe: ");
		scanf_s("%d", &a);

		Costam.zaw.cal = a;
	}

	if (wybor - 1 == 1) {
		float a;
		printf("\nPodaj liczbe: ");
		scanf_s("%f", &a);

		Costam.zaw.wym = a;
	}

	return Costam;
}

int main() {
	struct Dane Nowy = wczytaj();
}