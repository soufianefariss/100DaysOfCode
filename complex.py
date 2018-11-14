from math import sqrt

class Complex:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def add(self):
		return Number(self.x.re + self.y.re, self.x.im + self.y.im)
		
	def mul(self):
		return Number(self.x.re * self.y.re -self.x.im * self.y.im, self.y.re * self.x.im + self.x.re * self.y.im)

class Number:
	def __init__(self, re, im):
		self.re = re
		self.im = im
	
	def __str__(self):
		if self.re == 0 and self.im == 0:
			return("0")
		elif self.re > 0 and self.im > 0:
			return("%s + %si" % (str(self.re), str(self.im)))
		elif self.re < 0 and self.im < 0:
			return("-%s - %si" % (str(-self.re), str(-self.im)))
		elif self.im == 0 and self.re != 0:
			return ("%s" % str(self.re))
		elif self.im != 0 and self.re == 0:
			if self.im < 0:
				return ("-%si" % str(-self.im))
			else: 
				return ("%si" % str(self.im)) 
		elif self.re > 0 and self.im < 0:
			return ("%s - %si" %(str(self.re), str(-self.im)))
		else:
			return ("%s + %si" %(str(self.re), str(self.im)))
	
	def negation(self):
		self.re = -self.re
		self.im = -self.im
		return self
		
	def inversion(self):
		root = sqrt(self.re * self.im)
		self.re = (self.re / root)
		self.im = (self.im / root)
		return self
		

if __name__ == "__main__":
	while True:
		x1, y1 = map(int, input("Entrer un nombre complex (Exemple: 2 -3 --> 2 - 3i):\t").split()) 
		x2, y2 = map(int, input("Entrer un autre nombre complex:\t").split())
		
		n1 = Number(x1, y1)
		n2 = Number(x2, y2)
		print("\n\nLes deux nombres saisés: %s et %s"%(n1, n2))
		c = Complex(n1, n2)
		
		print("\nNégation: %s et %s\n\nSomme: %s\n\nProduit: %s" % (n1.negation(), n2.negation(), c.add(), c.mul()))
		
		entry = input("\nVoulez vous continuer? [y/n]\t")
		if not entry.lower().startswith("y"):
			break
	
