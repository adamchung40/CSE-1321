#Class:    CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

#Asking for height, weight, age, gender, and BMR
height = int(input("Enter your height (in inches) "))
weight = int(input("Enter your weight (in pounds) "))
age = int(input("Enter your age "))

gender = input("Enter your gender ")
if (gender == "female" or gender == "Female"):
    bmr = 655 + (4.35*weight) + (4.7*height) - (4.7*age)
elif (gender == "male" or gender == "Male"):
    bmr = 66 + (6.23*weight) + (12.7*height) - (6.8*age)

#Selecting level of exercise each week
lvl_exercise = 9
while (lvl_exercise != 0):
    lvl_exercise = int(input("Select your approximate level of exercise each week (Enter 0 to cancel the program)\n" +
    "1. You don't exercise\n" +
    "2. You engage in light exercise one to three days a week\n" +
    "3. You exercise moderately three to five times a week\n" +
    "4. You exercise intensely six to seven days a week\n" +
    "5. You exercise intensely six to seven days a week and have a physically active job "))
#Level 1
    if (lvl_exercise == 1):
        exercise = "Exercise 1 "
        dca = bmr * 1.2
        print(gender, end=", ")
        print(height, end='", ')
        print(weight, end='lbs, ')
        print("age", age, end=", ")
        print("BMR =", round(bmr, 2), end=", ")
        print(exercise, end=", ")
        print("DCA:", round(dca, 2))
#Level 2
    elif (lvl_exercise == 2):
        exercise = "Exercise 2 "
        dca = bmr * 1.375
        print(gender, end=", ")
        print(height, end='", ')
        print(weight, end='lbs, ')
        print("age", age, end=", ")
        print("BMR =", round(bmr, 2), end=", ")
        print(exercise, end=", ")
        print("DCA:", round(dca, 2))
#Level 3
    elif (lvl_exercise == 3):
        exercise = "Exercise 3 "
        dca = bmr * 1.55
        print(gender, end=", ")
        print(height, end='", ')
        print(weight, end='lbs, ')
        print("age", age, end=", ")
        print("BMR =", round(bmr, 2), end=", ")
        print(exercise, end=", ")
        print("DCA:", round(dca, 2))
#Level 4
    elif (lvl_exercise == 4):
        exercise = "Exercise 4 "
        dca = bmr * 1.725
        print(gender, end=", ")
        print(height, end='", ')
        print(weight, end='lbs, ')
        print("age", age, end=", ")
        print("BMR =", round(bmr, 2), end=", ")
        print(exercise, end=", ")
        print("DCA:", round(dca, 2))
#Level 5
    elif (lvl_exercise == 5):
        exercise = "Exercise 5 "
        dca = bmr * 1.9
        print(gender, end=", ")
        print(height, end='", ')
        print(weight, end='lbs, ')
        print("age", age, end=", ")
        print("BMR =", round(bmr, 2), end=", ")
        print(exercise, end=", ")
        print("DCA:", round(dca, 2))
		print()