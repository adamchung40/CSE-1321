grade1 = int(input("Enter the first grade "))
grade2 = int(input("Enter the second grade "))
grade3 = int(input("Enter the third grade "))
grade4 = int(input("Enter the fourth grade "))
grade5 = int(input("Enter the fifth grade "))

avg = (grade1+grade2+grade3+grade4+grade5)/5

#Highest Grade
high = grade1
if grade1 < grade2:
	high = grade2
if grade3 > high:
	high = grade3
if grade4 > high:
	high = grade4
if grade5 > high:
	high = grade5

#Lowest Grade
low = grade1
if grade1 > grade2:
	low = grade2
if grade3 < low:
	low = grade3
if grade4 < low:
	low = grade4
if grade5 < low:
	low = grade5

#Print statements
print("You entered: ", grade1, grade2, grade3, grade4, grade5)
print("Highest grade: ", high)
print("Lowest grade: ", low)
print("Average grade: ", avg)