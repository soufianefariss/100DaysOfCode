#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[]) {
	if (argc != 2)
		printf("Usage: collatz N");
	else {
		int counter = 0;
		int N = atoi(argv[1]);
		while (N != 1) {
			counter++;
			if (N % 2 == 0)
				N /= 2;
			else
				N = 3 * N + 1;
			printf("%4d", N);
		}
		printf("\n%d\n", counter);
	}
}
