x = int(input("Enter the x-coordinate "))
y = int(input("Enter the y-coordinate "))
points = (x,y)

if x == 0 and y == 0:
	location = "origin point."
elif y == 0:
	location = "x-axis."
elif x == 0:
	location = "y-axis."
elif x > 0 and y > 0:
	location = "first quadrant."
elif x < 0 and y > 0:
	location = "second quadrant."
elif x < 0 and y < 0:
	location = "third quadrant."
elif x > 0 and y < 0:
	location = "fourth quadrant."

#Print Statement
print(points, "is on the " + location)