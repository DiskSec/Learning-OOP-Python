class BankAccount:
	def __init__(self, account_number, balance):
		self.__account_number = account_number # Private attribute
		self.__balance = balance			   # Private attribute

	def deposit(self, amount):
		self.__balance += amount

	def withdraw(self, amount):
		if amount <= self.__balance:
			self.__balance -= amount
		else:
			print("Insufficient funds")

	def get_balance(self):
		return self.__balance

# Create a BankAccount instance
account_luksi = BankAccount("5673", 3000)
account_zdravko = BankAccount("1111", 500)

# Access private attributes using public methods
print(account_luksi.get_balance())		# Output: 3000
print(account_zdravko.get_balance())	# Output: 500
account_luksi.deposit(500)
account_zdravko.deposit(10000)

account_luksi.withdraw(100)
account_zdravko.withdraw(2000)
print(account_luksi.get_balance())
print(account_zdravko.get_balance())

print(account_luksi.account_number)
