from array import *

def gradeScale(grades):
	if grades >= 90 and grades <= 100:
		return "grade is A"
	elif grades >= 80 and grades <= 89:
		return "grade is B"
	elif grades >= 70 and grades <= 79:
		return "grade is C"
	elif grades >= 60 and grades <= 69:
		return "grade is D"
	else:
		return "grade is F"

def main():
	class_size = int(input("Enter the size of the class "))

	class_grades = array('i', [0]*class_size)

	for i in range(len(class_grades)):
		grade = int(input("Please enter the grade for student " + str(i) + " "))
		class_grades[i] = grade
		
	for i in range(len(class_grades)):
		print("Student", i, "score is", class_grades[i], "and", gradeScale(class_grades[i]))
main()