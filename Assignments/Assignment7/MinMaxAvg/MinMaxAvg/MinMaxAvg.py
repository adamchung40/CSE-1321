from array import *

def minMaxAvg(grades):
	highest = grades[0][0] #Highest Grade
	for row in grades:
		for column in row:
			if highest < column:
				highest = column

	lowest = grades[0][0] #Lowest Grade
	for row in grades:
		for column in row:
			if lowest > column:
				lowest = column

	total = 0 #Class Avg
	amount = 0
	for row in grades:
		for column in row:
			total += column
			amount += 1
	avg = round(total/amount,2)

	return print("Highest grade: ", highest,
				"\nLowest grade:  ", lowest,
				"\nClass Average: ", avg)

def main():
#Sample Run 1
	grades = [[38, 44, 22, 91],
			  [81, 60, 71, 80],
			  [99, 49, 98, 63],
			  [71, 33, 93, 49]]
	print('Array grades:')
	for row in grades:
		for column in row:
			print(column,end=' ')
		print()
	print()
	minMaxAvg(grades)

	print()
#Sample Run 2
	grades2 =[[60, 88, 98, 100],
			  [87, 75, 68, 93],
			  [95, 86, 98, 73],
			  [56, 73, 88, 71]]
	print('Array grades 2:')
	for row in grades:
		for column in row:
			print(column,end=' ')
		print()
	print()
	minMaxAvg(grades2)
main()
