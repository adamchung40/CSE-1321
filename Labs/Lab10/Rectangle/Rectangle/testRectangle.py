from Rectangle import RectangleClass

def main():
	r1 = RectangleClass()
	print("First Object: ")
	print("\tHeight:", r1.getHeight(), "unit")
	print("\tWidth:", r1.getWidth(), "unit")
	print("\tArea:", r1.getArea(), "unit")
	print("\tPerimeter:", r1.getPerimeter(), "units")

	r2 = RectangleClass(5,6)
	print("Second Object: ")
	print("\tHeight:", r2.getHeight(), "unit")
	print("\tWidth:", r2.getWidth(), "unit")
	print("\tArea:", r2.getArea(), "units")
	print("\tPerimeter:", r2.getPerimeter(), "units")
main()
