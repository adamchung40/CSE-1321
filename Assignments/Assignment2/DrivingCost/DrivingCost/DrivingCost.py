#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

#Input prompts
miles = float(input("Distance traveled (miles): "))
mpg = float(input("Miles per gallon (miles): "))
ppg = float(input("Price per gallon (dollars): "))

#Calculations
trip_cost = (miles/mpg) * ppg

#Print Statement
print("Trip cost (dollars): ", trip_cost)