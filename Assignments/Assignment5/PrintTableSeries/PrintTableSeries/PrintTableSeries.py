def displaySums(num):
	sum = 0
	for i in range (1,num+1):
		sum += i/(i+1)
	return sum

def main():
	num = int(input("Enter a number "))
	print("i\t Sum(i)")
	for i in range (1,num+1):
		print(i,"\t",displaySums(i))
main()