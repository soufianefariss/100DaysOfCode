from __future__ import print_function

def fibonacci(N):
	n, m = 1, 0
	for i in range(N):
		n = n + m
		m = n - m
	return n

def shell():
	"""
	
	Console Function to create the interactive Shell.
	
	"""
	print("Welcome to Fibonacci Sequence Calculator")
	
	while True:
		print(">>> ", end='')
		entry = input()
		if entry == "quit":
			break
		if not entry.isdigit():
			print("Please enter a postive integer.")
		else:
			print(fibonacci(int(entry)))


if __name__ == "__main__":
	shell()
