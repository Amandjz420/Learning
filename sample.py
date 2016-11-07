#Program that documents and searches for stocks and can find higher priced stocks.

#This function creates two lists, name of the stock and the price of the stock, and has the inputs from the user put in to them respectively.
def getStocks():
    i = 0
    stockNames = [] 
    stockPrices = []
    userDone = 0 
    while i < 1:
        name = raw_input("Enter the name of a stock (done if finished): ")
        if 'done' in name:
            i = i + 1
        else:
            stockNames.append(name)
            price=""
            while True:
                try :
                    price = int(raw_input("Enter the price of stock: "))
                except ValueError:
                    print("input integer only")
                else:
                    break
            stockPrices.append(price)
    return(stockNames, stockPrices)


#This function searches the lists of stock names, and upon finding user's inputted stock name, returns its associated value
def searchStock(stockNames, stockPrices, s):
    try:
       i = stockNames.index(s)
    except ValueError:
        return -1
    else:
        return stockPrices[i]

#This function is used to locate stocks with higher values as compared by user's input
def printStock(stockNames, stockPrices, p):
    num = int(p)
    for i in range(len(stockPrices)):
        if(stockPrices[i]>num):
            print(str(i)+". "+stockNames[i])
    return

#Main function for the program that calls the other functions into it, in order, to fulfill program requirements
def main():
    
#Assigns variables n and p to the lists in the getStocks function
    n,p = getStocks()

#Finds the price of a stock given it's input name
    stock = raw_input("Enter the name of a stock you would like to find the price of: ")
    price = searchStock(n,p,stock)
    print("The price of that stock is: " + str(price))


#Finds if any other stocks have a higher value than the stock inputted by user
    maxPrice = ""
    while True:
                try :
                    maxPrice = int(raw_input("\nEnter a price to find a stock with higher values: "))
                except ValueError:
                    print("input integer only")
                else:
                    break

    if (max(p) <= maxPrice):
        print("\nThere are no stocks higher than "+ str( maxPrice))
    else:
        print("\nThe following stocks have prices higher than the " +str(maxPrice) +"\n")
        printStock(n,p,maxPrice)
        
main()
