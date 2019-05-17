#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

account_num = int(input("Please enter your account number "))
service_code = input("Please enter your service type (R for Regular or P for Premium) ")

if (service_code == "r" or service_code == "R"):
	service_type = "Regular"
	service_num = int(input("Enter number of minutes "))
	if service_num > 50:
		amount_due = 15 + (service_num - 50) * .50
	else:
		amount_due = 15
elif (service_code == "p" or service_code == "P"):
	service_type = "Premium"
	daytime_num = int(input("Enter number of minutes for daytime calls "))
	if daytime_num > 50:
		total_day = (daytime_num - 50) * .10
	else:
		total_day = 0
	nighttime_num = int(input("Enter number of minutes for nighttime calls "))
	if nighttime_num > 100:
		total_night = (nighttime_num - 100) * .10
	else:
		total_night = 0
	amount_due = total_day + total_night + 25.00

#Print Statements
print("Account number: ", account_num)
print("Service type: ", service_type)
if service_code == "r" or service_code == "R":
	print("Total minutes: ", service_num)
elif service_code == "p" or service_code == "P":
	print("Daytime minutes: ", daytime_num)
	print("Nighttime minutes: ", nighttime_num)
print("Amount due: $", amount_due)