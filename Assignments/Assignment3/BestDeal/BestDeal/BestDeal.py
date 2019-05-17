#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

small_weight = int(input("Enter the weight of the small box "))
small_price = int(input("Enter the price of the small box "))
large_weight = int(input("Enter the weight of the large box "))
large_price = int(input("Enter the price of the large box "))

small_deal = small_price / small_weight
large_deal = large_price / large_weight

if (small_deal > large_deal):
	better_deal = "The large box is a better deal "
elif (small_deal < large_deal):
	better_deal = "The small box is a better deal "
else:
	better_deal = "Both boxes are of the same value "

#Print Statements
print("Small box weight: " + str(small_weight) + " Pounds")
print("Small box price: ", str(small_price) + " Dollars")
print("Large box weight: ", str(large_weight) + " Pounds")
print("Large box price: ", str(large_price) + " Dollars")
print("Judgement: ", better_deal)