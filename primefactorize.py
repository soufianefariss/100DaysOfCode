

def trial_division(n):
	factors = []
	f = 2
	
	while n > 1:
		if not n % f:
			factors.append(str(f))
			n /= f
		else:
			f += 1
	return factors
	
def shell():
	print("Welcome to Prime Factorizer!")
	
	while True:
		print(">>> ", end='')
		entry = input()
		if (entry == "quit"):
			break
		elif not entry.isdigit():
			print("Please enter a positive integer.")
		else:
			print(" * ".join(trial_division(int(entry))))

if __name__ == "__main__":
	shell()
