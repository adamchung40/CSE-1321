#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

annual_income = int(input("Enter your annual income "))

if (annual_income <= 50000):
	tax_bracket = "5%"
	tax_due = annual_income * .05
elif (50000 < annual_income and annual_income <= 200000):
	tax_bracket = "10%"
	tax_due = (50000 * .05) + (annual_income - 50000) * .10
elif (200000 < annual_income and annual_income <= 400000):
	tax_bracket = "15%"
	tax_due = (50000 * .05) + (150000 * .10) + (annual_income - 200000) * .15
elif (400000 < annual_income and annual_income <= 900000):
	tax_bracket = "25%"
	tax_due = (50000 * .05) + (150000 * .10) + (200000 * .15) + (annual_income - 400000) * .25
elif (900000 < annual_income):
	tax_bracket = "35%"
	tax_due = (50000 * .05) + (150000 * .10) + (200000 * .15) + (500000 * .25) + (annual_income - 900000) * .35

#Print Statements
print("Annual Income: ", annual_income)
print("Tax Bracket: ", tax_bracket)
print("Tax due amount: $", tax_due)