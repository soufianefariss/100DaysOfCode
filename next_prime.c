#include <stdio.h>
#include <math.h>

int isPrime(int n) {
	if (n == 2) {
		return 1;
	} else if (n % 2 == 0) {
		return 0;
	}
	for (int i = 3; i <= pow(n, 0.5); i += 2) {
		if (n % i == 0)
			return 0;
	}
	
	return 1;
}

int generatePrime(int currentPrime) {
	
	while (1) {
		currentPrime++;
		if (isPrime(currentPrime)) {
			break;
		}
		
	}
	return currentPrime;
}

void main(void) {
	int currentPrime = 2;
	char answer;
	
	while (1) {
		printf("Would you like to the see the next prime number? [y/n]\t");
		scanf(" %c", &answer);
		if (answer == 'Y' || answer == 'y') {
			printf("%d\n", currentPrime);
			currentPrime = generatePrime(currentPrime);
		} else {
			printf("\n");
			break;
		}
	}
}
