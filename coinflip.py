from random import randint

def main():
	"""
	prints a dict containing all the outcomes  
	"""
	
	outcomes = {}
	tries = int(input("Enter the number of tries to stimulate:\t"))
	
	i = 0
	while (i < tries):
		outcomes[i] = randint(0, 1) # generates a random integer (0 or 1)
		i += 1
	
	tails, heads = sum(value == 0 for value in outcomes.values()), sum(value == 1 for value in outcomes.values())
	
	for key, value in outcomes.items():
		result = "tail" if not value else "head" 
		print(key, "  :\t", result)

	print("\nNbr of tails: %d\nNbr of heads: %d" %(tails, heads))
	
if __name__ == "__main__":
	main()
