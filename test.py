class Cat:
	def __init__(self, years, name, color):
		self.years = years
		self.name = name
		self.color = color


cat = Cat(20, "Stupid", "Red")

attributes = [cat.years, cat.name, cat.color]
print(attributes)
