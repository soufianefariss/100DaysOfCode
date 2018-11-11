#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX 18

int main(int argc, char *argv[]) {
	if (argc != 2) {
		printf("Usage: PIapprox\n");
		return -1;
	}
	
	int N = atoi(argv[1]), M;
	if (N < 1) {
		printf("Error. Please enter a positive integer\n");
		return -1;
	} else if (N > MAX) {
		M = MAX;
	} else {
		M = N;
	}
	
	double digit = 0.0;
	for (int i = 0; i < M; i++) {
		digit += ((pow(16, -i))) * (((4.0 / (8 * i + 1))) - ((2.0 / (8 * i + 4))) - ((1.0 / (8 * i + 5))) - ((1.0 / (8 * i + 6))));
	}
	printf("Pi is: %.*f\n", M, digit);
	
	return 0;
	
}
