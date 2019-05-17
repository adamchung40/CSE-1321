from BankAccount import bankAccount
def main():
	myObject = bankAccount(123456, 10000, 0.025, "Sun Nov 2 14:18:16 EDT 2017")
	myObject.withdraw(3500)
	myObject.deposit(500)
	print("Account Balance:", myObject.getBalance())
	print("Money earned monthly interest:", myObject.getMonthlyInterest())
	print("Account was opened on:", myObject.getDateCreated())
main()