def isValid(width,height):
	if (width + height > 30):
		return ""
	else:
		while (width + height < 30):
			print("This is invalid rectangle. Try again.\n ")
			width = int(input("Enter the width of the rectangle "))
			height = int(input("Enter the height of the rectangle "))
#Area
def Area(width,height):
	area = width * height
	return area
#Perimeter
def Perimeter(width,height):
	perimeter = (2*width) + (2*height)
	return perimeter

def main():
	width = int(input("Enter the width of the rectangle "))
	height = int(input("Enter the height of the rectangle "))
	print(isValid(width,height))
	print("Entered width:", width)
	print("Entered height ", height)
	print("Area: ", Area(width,height))
	print("Perimeter: ", Perimeter(width,height))
main()