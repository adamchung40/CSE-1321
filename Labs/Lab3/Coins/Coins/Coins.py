#Amount of coins
quarters = int(input("Enter number of quarters: "))
dimes = int(input("Enter number of dimes: "))
nickels = int(input("Enter number of nickels: "))
pennies = int(input("Enter number of pennies: "))

#Print statements
print("You entered ", quarters, "quarters")
print("You entered ", dimes, "dimes")
print("You entered ", nickels, "nickels")
print("You entered ", pennies, "pennies")

#Calculating the Total
total = (quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)
dollars = total // 100
cent = total % 100

#Print Statements
print("Your total is " + str(dollars) + " dollars and " + str(cent) + " cents")