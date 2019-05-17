def locateLargest(newArray):
	max = newArray[0][0]
	row = 0
	column = 0
	for r in range(len(newArray)):
		for c in range(len(newArray[0])):
			if max < newArray[r][c]:
				max = newArray[r][c]
				row = r
				column = c
	print("First largest value is located at row", row, "and column", column)

def main():
#Sample Run 1:
	newArray = [[9,  1,   2,  4 ], 
				[2,  11,  18, 20],
				[3,  20,  3,  12]]
	print("The entered matrix: ")
	for row in newArray:
		for column in row:
			print(column, end=' ')
		print()
	print()
	locateLargest(newArray)
	print()
#User Input
	newArray2 = [[0, 0, 0, 0], 
				 [0, 0, 0, 0],
				 [0, 0, 0, 0]]
	for r in range(len(newArray2)):
		for c in range(len(newArray2[0])):
			num = int(input("Enter a number for Row: " + str(r) + " Column: " + str(c) + " → ")) #User Input
			newArray2[r][c] = num
	print()
	for row in newArray2:
		for column in row:
			print(column, end=' ')
		print()
	print()
	locateLargest(newArray2)

main()
