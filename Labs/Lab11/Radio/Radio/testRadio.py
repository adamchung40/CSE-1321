from Radio import radio
def main():
	radio1 = radio()
	print("Turn radio on:")
	radio1.turnOn()
	radio1.toString()

	print("Turn volume up by 3:")
	radio1.volumeUp(3)
	radio1.toString()

	print(radio1.staion)

	print("Move station up by 5:")
	radio1.stationUp(5)
	radio1.toString()

	print("Turn volume down by 1:")
	radio1.volumeDown(1)
	radio1.toString()

	print("Move station up by 3:")
	radio1.stationUp(3)
	radio1.toString()

	print("Turn off radio.")
	radio1.turnOff()
	radio1.toString()

	print("Turn volume up by 2:")
	radio1.volumeUp(1)
	radio1.toString()

	print("Turn station down by 2:")
	radio1.stationDown(2)
	radio1.toString()
	
	print(radio1.staion)
main()
