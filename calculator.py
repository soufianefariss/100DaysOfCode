class Calculator:
	"""
	This is a simple calculator. 
	Available operators are: +, -, × and /.
	"""
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def add(self):
		"""This adds two numbers"""
		print("%s + %s = %s" % (a, b, a + b))
	
	def sub(self):
		"""This substracts two numbers"""
		print("%s - %s = %s" % (a, b, a - b))
	
	def mul(self):
		"""This multiplies two numbers"""
		print("%s × %s = %s" % (a, b, a * b))
	
	def div(self):
		"""This divides two numbers"""
		print("%s / %s = %s" % (a, b, round(a / b, 3)))

#if __name__ == "__main__":
print("Welcome to my calculator.\nFor help, please use the command 'help(calculator)'")
while True:
	a = int(input("Enter a number: "))
	b = int(input("Enter another number: "))
	calc = Calculator(a, b)
	
	calc.add()
	calc.sub()
	calc.mul()
	calc.div()
	
	entry = input("Do you want to try again? [y/n]\t")
	if not entry.lower().startswith("y"):
		break
	
		
		
		
