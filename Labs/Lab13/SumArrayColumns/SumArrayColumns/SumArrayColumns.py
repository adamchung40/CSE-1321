import random
def sumColumn(newArray):
	for c in range(len(newArray[0])):
		total = 0
		for r in range(len(newArray)):
			total += newArray[r][c]
		print("Sum of column ", c, "is", total)


def main():
	newArray = [ [0, 0, 0, 0],
				 [0, 0, 0, 0],
				 [0, 0, 0, 0]]
	for x in range(len(newArray)):
		for y in range(len(newArray[0])):
			num = random.randrange(50)
			#num = int(input("Enter a number for Row: " + str(x) + " Column: " + str(y) + " → ")) #User Input
			newArray[x][y] = num
	print()
	print("The entered matrix:")
	for row in newArray:
		for column in row:
			print(column, end=' ')
		print()
	print()
	sumColumn(newArray)
main()