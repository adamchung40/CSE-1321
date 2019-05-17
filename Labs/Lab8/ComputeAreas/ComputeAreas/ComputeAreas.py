#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 8
import math

def squareArea(side):
	area = side*side
	return area
def rectangleArea(width,length):
	area = width * length
	return area
def circleArea(radius):
	area = radius**2 * math.pi
	return area
def triangleArea(base,height):
	area = (base*height)/2
	return area

def main():
	#Area of Square
	square_side = float(input("Enter length side of the square "))
	print("Square side: ", square_side)
	print("Square area: ", squareArea(square_side))
	print()
	#Area of Rectangle
	rectangle_width = float(input("Enter width of the rectangle "))
	rectangle_length = float(input("Enter length of the rectangle "))
	print("Rectangle width ", rectangle_width)
	print("Rectangle length ", rectangle_length)
	print("Rectangle area ", rectangleArea(rectangle_width,rectangle_length))
	print()
	#Area of Circle
	radius = float(input("Enter the radius of the circle "))
	print("Circle radius ", radius)
	print("Circle area ", circleArea(radius))
	print()
	#Area of Triangle 
	base = float(input("Enter the base of the triangle "))
	height = float(input("Enter the height of the triangle "))
	print("Triangle base:", base)
	print("Triangle height:", height)
	print("Triangle area:", triangleArea(base,height))
	print()
main()