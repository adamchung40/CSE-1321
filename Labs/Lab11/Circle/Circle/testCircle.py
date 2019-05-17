from Circle import circle
def main():
	c1 = circle() #Default Circle Object
	print("The radius is", c1.getRadius())
	print("The area is", c1.getArea())
	print("The perimeter is", c1.getPerimeter(), "\n")

	c1.setRadius(10) #Radius is set to 10
	print("The radius is", c1.getRadius())
	print("The area is", c1.getArea())
	print("The perimeter is", c1.getPerimeter())
main()
