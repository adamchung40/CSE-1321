#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2
num = 1
x = ''
x_pos = ''
max = 0

while (num != '0'):
	num = input("Enter postive integers (0 to quit): ")
	if int(num) > 0:
		x_pos += num
		if max < int(num):
			max = int(num)
	x += num
	x += " "
print(x)
print(x_pos)
print("Largest value: ", max)
counter = 0
for char in x_pos:
    if int(char) == max:
        counter += 1
print("Occurrences: ", counter)    


if (num == 0):
	print("No values were entered. ")