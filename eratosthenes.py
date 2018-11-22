
def main(n):
	prime = (n + 1) * [True]
	p = 2
	while (p ** 2 <= n):
		if prime[p]:
			for i in range(p * 2, n + 1, p):
				prime[i] = False
		p += 1
	for p in range(2, n):
		if prime[p]:
			print(p)
			
if __name__ == "__main__":
	n = int(input("Entrer n:\t"))
	main(n)
