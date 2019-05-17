def addHours(newArray):
	print('\nEmployee#\t Weekly Hours')
	num = 1
	for x in newArray:
		total_hours = 0
		for y in x:
			total_hours += y
		print(num,'\t\t', total_hours)
		num += 1
	
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
	print()
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
	print()
	addHours(newArray1)
	print()
main()
