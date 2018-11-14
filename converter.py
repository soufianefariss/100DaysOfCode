class Converter:
	def __init__(self, number):
		self.number = number
	
	def toBinary(self):
		binary = ""
		while self.number > 0:
			binary += str(self.number % 2)
			self.number //= 2
		return binary[::-1]
	
	def toDecimal(self):
		decimal = 0
		max_power = len(str(self.number))  - 1
		for i in str(self.number):
			decimal += int(i) * (2 ** max_power)
			max_power -= 1
		return decimal
	
if __name__ == "__main__":
	entry = int(input("Entrer a number: "))
	number = Converter(entry)
	method = input("Convertir to binary or to decimal [b/d]")
	if method.startswith("b"):
		print(number.toBinary())
	else:
		print(number.toDecimal())
