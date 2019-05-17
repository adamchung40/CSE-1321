def isEquivalent(arrayA,arrayB):
	for r in range(len(arrayA)):
		for c in range(len(arrayA[0])):
			if arrayA[r][c] == arrayB[r][c]:
				print(end='')
			else: 
				return "The arrays are not equivalent."
	return "The arrays are equivalent."

def main():
	newArrayA =[ [0, 0, 0],
				 [0, 0, 0],
				 [0, 0, 0]]
	print("Enter a number for Matrix A:")
	for r in range(len(newArrayA)):
		for c in range(len(newArrayA[0])):
			num = int(input("Row: " + str(r) + " Column: " + str(c) + " → ")) #User Input
			newArrayA[r][c] = num
	print()
	newArrayB =[ [0, 0, 0],
				 [0, 0, 0],
				 [0, 0, 0]]
	print("Enter a number for Matrix B:")
	for r in range(len(newArrayB)):
		for c in range(len(newArrayB[0])):
			num = int(input("Row: " + str(r) + " Column: " + str(c) + " → ")) #User Input
			newArrayB[r][c] = num
	print()
	print("Matrix A:") #Matrix A
	for row in newArrayA:
		print("\t", end='')
		for column in row:
			print(column, end=' ')
		print()
	print()
	print("Matrix B:") #Matrix B
	for row in newArrayB: 
		print("\t", end='')
		for column in row:
			print(column, end=' ')
		print()
	print()
	print("Judgement:", isEquivalent(newArrayA,newArrayB))

main()

