#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

def case_10_handler():
    print("That grade is a perfect score. Well done.")
def case_9_handler():
    print("That grade is well above average. Excellent work.")
def case_8_handler():
    print("That grade is above average. Nice job.")
def case_7_handler():
    print("That grade is above average work")
def case_6_handler():
    print("That grade is not good, you should seek help!")
def default_handler():
    print("That grade is not passing")

def switch_function(switch):​
    handler = {
        10: case_10_handler,
        9: case_9_handler,
        8: case_8_handler,
        7: case_7_handler,
        6: case_6_handler
    }
    return handler.get(switch, default_handler)()

def main():
    grade = int(input("Enter your grade"))
    conditions = int(grade/10)
    print("You entered ", conditions)
    switch_function(conditions)

if __name__== "__main__":
    main()
