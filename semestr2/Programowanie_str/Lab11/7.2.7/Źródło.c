#include <stdio.h>
#include <stdlib.h>

struct zespolone {
	double Re;
	double Im;
};

struct zespolone dodawanie(struct zespolone A, struct zespolone B) {
	struct zespolone wynik = { A.Re + B.Re, A.Im + B.Im };
	return wynik;
}

int main() {
	struct zespolone A = { 4, 7 };
	struct zespolone B = { 8, 3 };

	printf("Re = %f\nIm = %f", dodawanie(A, B).Re, dodawanie(A, B).Im);
}