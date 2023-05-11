#include <stdio.h>
#include <stdlib.h>

struct trojkat {
	float a, b, c;
};

void przepisz(struct trojkat A, struct trojkat* B) {
	*B = A;
}

int main() {
	struct trojkat Troj1 = { 3,6,9 };
	struct trojkat Troj2;

	przepisz(Troj1, &Troj2);
	printf("%f %f %f", Troj2.a, Troj2.b, Troj2.c);
}
