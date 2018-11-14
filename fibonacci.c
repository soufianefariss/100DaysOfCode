#include <stdio.h>
#include <ctype.h>
#include <string.h>

unsigned long int fibonacci(int N) {
	int n, m, i = 1, 0, 0;
	while (i < N) {
		n = n + m;
		m = n - m;
		i++;
	}
	return n;
}

void main(void) {
	printf("Welcome to the interactive Fibonacci Sequence calculator\n");
	char N[10], quit[10];
	
	while (1) {
	 	printf(">>> ");
	 	scanf(" %s", &N);
	 	strcpy(quit, "quit")
	 	
	 	if (!(strcmp(quit, "quit"))) {
	 		break;
	 	} else if (!(isdigit(N))) {
	 		printf("Please enter a positive integer.\n");
	 	} else {
	 		printf("%ld\n", fibonacci(N));		
	 	}
	}
}
