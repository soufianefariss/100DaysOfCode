#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
	if (argc != 2)
		printf("Usage: eratosthenes N\n");
	else {
		int n = atoi(argv[1]);
		int prime[n + 1], p = 2;
		for (int i = 0; i < n; i ++) {
			prime[i] = 1;
		}
		
		while (p * p <= n) {
			if (prime[p]) {
				for (int i = p * 2; i < n + 1; i += p) {
					prime[i] = 0;
				}
			}
			printf("%d\n", p);
			p += 1;
		}
		
		for (int i = 2; i < n; i++) {
			if (prime[i])
				printf("%d\n", i);
		}
	}
}
