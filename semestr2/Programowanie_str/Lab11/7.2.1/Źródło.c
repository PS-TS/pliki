#include <stdio.h>
#include <stdlib.h>

struct trojkat {
	float a;
	float b;
	float c;
};

float obwodtroj(struct trojkat A) {
	return A.a + A.b + A.c;
}

int main() {
	struct trojkat A = {5, 3, 7};
	printf("%f", obwodtroj(A));
}