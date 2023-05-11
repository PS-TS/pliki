#include <stdio.h>
#include <stdlib.h>

enum zwierzaki {
	Pies = 0,
	Kot = 1,
	Chomik = 2,
	Krolik = 3,
	Papuga = 4,
	Swinka_Morska = 5
};

int main() {
	enum zwierzaki gryzon1 = Chomik;
	enum zwierzaki gryzon2 = Swinka_Morska;
	printf("%d\n%d", gryzon1, gryzon2);
}
