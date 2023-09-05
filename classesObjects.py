class Dog:
	def __init__(self, name, breed, age):
		self.name = name
		self.breed = breed
		self.age = age

	def bark(self):
		return f"{self.name} says Woof!"

	def play(self, duration):
		self.duration = duration
		return f"{self.name} is playing for {self.duration} minutes"


# Create objects (instances) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 22)
dog2 = Dog("Sadie", "Poodle", 45)
dog3 = Dog("King", "Pitbull", 67)

# Access object attribute and call methods
print(dog1.name)
print(dog2.breed)
print(dog1.bark())
dog3_attr = [dog3.name, dog3.breed]
for x in dog3_attr:
	print(x)

ages = {"dog1": dog1.age,"dog2": dog2.age,"dog3": dog3.age}
print(ages)
for age in ages.items():
	print(set(age))

all_dogs = [dog1, dog2, dog3]
for each in all_dogs:
	if each.name == "Buddy":
		print(each.play(30))
	elif each.name == "Sadie":
		print(each.play(40))
	else:
		print(each.play(50))

