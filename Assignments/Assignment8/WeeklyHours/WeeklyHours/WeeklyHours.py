def addHours(newArray):
#Day each worked worked the most hrs
	num = 1
	for r in range(len(newArray)):
		c = 0
		num_day = c
		max = newArray[r][c]
		for c in range(len(newArray[0])):
			if max < newArray[r][c]:
				max = newArray[r][c]
				num_day = c
		if num_day == 0:
			day = "Monday"
		elif num_day == 1:
			day = "Tuesday"
		elif num_day == 2:
			day = "Wednesday"
		elif num_day == 3:
			day = "Thursday"
		elif num_day == 4:
			day = "Friday"
		elif num_day == 5:
			day = "Saturday"
		elif num_day == 6:
			day = "Sunday"
		print("Employee", num, "worked most hours on " + day)
		num += 1
#Which worker worked the most hrs?
	print('\nEmployee#\t Weekly Hours')
	employee = list()
	num = 1
	for row in newArray:
		total_hours = 0
		for column in row:
			total_hours += column
		employee.append(total_hours)

	min = employee[0] #Min Hours
	for i in employee:
		if i < min:
			min = i
	max = employee[0] #Max Hours
	for j in employee:
		if j > max:
			max = j
	for i in employee: #Med Hours
		if i > min and i < max:
			med = i
#Print Statements
	print((employee.index(min))+1, '\t\t', min)
	print((employee.index(med))+1, '\t\t', med)
	print((employee.index(max))+1, '\t\t', max)
	
def main():
#Sample Data 1
	newArray = [ [5, 3, 2, 9, 6, 5, 7],
				 [7, 6, 8, 5, 5, 4, 5],
				 [1, 2, 2, 1, 5, 8, 7] ]
	print("Employees Data:")
	print("\t\tMon \tTues \tWed \tThur \tFri \tSat \tSun")
	print("Employee1\t", end='')   #Employee 1
	for i in range(7):
		print(newArray[0][i], end='\t')
	print("\nEmployee2\t", end='') #Employee 2
	for i in range(7):
		print(newArray[1][i], end='\t')
	print("\nEmployee3\t", end='') #Employee 3
	for i in range(7):
		print(newArray[2][i], end='\t')
	print("\n")
	addHours(newArray)
	print()
#Sample Data 2
	newArray1 =[ [10, 2, 7, 2, 0, 3, 8],
				 [5,  6, 1, 5, 1, 4, 2],
				 [1,  5, 2, 6, 4, 8, 7] ]
	print("Employees Data:")
	print("\t\tMon \tTues \tWed \tThur \tFri \tSat \tSun")
	print("Employee1\t", end='')   #Employee 1
	for i in range(7):
		print(newArray1[0][i], end='\t')
	print("\nEmployee2\t", end='') #Employee 2
	for i in range(7):
		print(newArray1[1][i], end='\t')
	print("\nEmployee3\t", end='') #Employee 3
	for i in range(7):
		print(newArray1[2][i], end='\t')
	print("\n")
	addHours(newArray1)
	print()
main()
