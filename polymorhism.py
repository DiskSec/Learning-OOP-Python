class Shape:
	def area(self):
		pass

class Rectangle(Shape):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14 * self.radius ** 2

# Create instances of different shapes
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Use polymorphism to calculate areas
shapes = [rectangle, circle]
for shape in shapes:
	print(f"Area: {shape.area()}")
