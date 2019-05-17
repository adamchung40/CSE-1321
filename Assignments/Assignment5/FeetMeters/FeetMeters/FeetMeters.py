#Feet to Meters
def feetToMeters(feet):
    meters = feet * 0.305
    return round(meters, 3)
#Meters to Feet
def metersToFeets(meters):
    feets = meters * 3.279
    return round(feets, 3)

def main():
    print("Feet\t" + "Meter\t\t" + "Meter\t" + "Feet")
    for i in range (1,21):
        j = str(feetToMeters(i))
        k = str(metersToFeets(i))
        print(str(i) + "\t" + j + "\t\t" + str(i) + "\t" + k)
		#print('{}\t{}\t\t{}\t{}'.format(str(i), j, str(i), k))
main()
