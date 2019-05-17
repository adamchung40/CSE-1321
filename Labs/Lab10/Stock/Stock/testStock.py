from Stock import Stocks

def main():
#Google Stocks
	stock1 = Stocks("GOG","Google")
	stock1.setClosingPrice(134.67)
	stock1.setCurrentPrice(131.98)
	print(stock1.getName(), "stocks:")
	print("\t Symbol:", stock1.getSymbol())
	print("\t Closing price:", stock1.previousClosingPrice)
	print("\t Current price:", stock1.currentPrice)
	print("\t Change percent:", stock1.getChangePercent(),"\b%")
	stock1.toString()
	print()
#Mircosoft Stocks
	stock2 = Stocks("MSF","Mircosoft")
	stock2.setClosingPrice(156.52)
	stock2.setCurrentPrice(161.22)
	print(stock2.getName(), "stocks:")
	print("\t Symbol:", stock2.getSymbol())
	print("\t Closing price:", stock2.previousClosingPrice)
	print("\t Current price:", stock2.currentPrice)
	print("\t Change percent:", stock2.getChangePercent(),"\b%")
	stock2.toString()
main()

