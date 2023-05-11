#include <stdio.h>
#include <stdlib.h>

union super_int{
	int cal;
	unsigned int calbez;
};

int main() {
	union super_int n;
	n.cal = -6;
	printf("%d\n", n.cal);
	n.calbez = -6;
	printf("%d", n.calbez);
}