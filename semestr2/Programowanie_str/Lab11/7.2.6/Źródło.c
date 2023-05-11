#include <stdio.h>
#include <stdlib.h>

struct punktND {
	int wym;
	float* wspolrzedne;
};

int main() {
	float* wymiary1 = malloc(3 * sizeof(float));
	wymiary1[0] = 4;
	wymiary1[1] = 7;
	wymiary1[2] = 12;

	struct punktND A = { 3, wymiary1 };

	for (int i = 0; i < 3; i++) {
		printf("%f ", A.wspolrzedne[i]);
	}
	printf("\nIlosc wymiarow = %d", A.wym);
}