class Monkey:
	def monkey(self, name):
		self.name = name
		return f"I am {self.name}"


class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		pass

class Dog(Animal, Monkey):
	def speak(self):
		return f"{self.name} says Woof!"

class Cat(Animal):
	def speak(self):
		return f"{self.name} says Meow!"

# Create instance of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the overriden 'speak' method
print(dog.speak())
print(cat.speak())
print(dog.monkey("dog"))
#print(cat.monkey())
