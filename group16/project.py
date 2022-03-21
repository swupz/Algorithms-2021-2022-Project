#from . import utils

#Prepare takes the file data and stores it in a dictionary ("stocks")
#In this dictionary, each unique stock name is a key. A key's associated value is a list 
#comprised of all the stock data associated with that particular key (i.e., stock name)
def prepare(filename : str):
    
    #Prints the name of the file that has been inputted
    print('Reading file {}'.format(filename))

    #Global variables
    global file, stocks, totals, mins, maxs
        
    #The file
    file = open(filename, "r")
    
    #The stocks dictionary
    stocks = {}
    
    #The totals dictionary
    #it stores the sum of all prices for a particular stock
    #the stock name is the key and the value is the sum of all prices for that stock
    totals = {}
    
    #The min and max dictionaries
    #they store the minimum price and maximum price (respectively) for each stock
    #the stock name is the key and the value is the min or max of all prices for that stock
    mins = {}
    maxs = {}
    
    #The first line of the file
    fileLine = file.readline()
    
    #While the current line of the file is not empty (i.e, we haven't reached the end of the file yet)
    while fileLine != "":
        #The current line of the file is split by "," and the output is a list of 4 items
        record = fileLine.split(',')
        record[-1] = record[-1][:0-2]
                
        #If the stock name is already a key in the stocks dictionary, simply add the new 
        #record to the list that is the value for that stock's key
        if record[0] in stocks.keys():
            stocks[record[0]].append(record)
            
            #Add the record's price to the particular stock's sum of all prices
            totals[record[0]] = int(record[2]) + totals[record[0]]
            
            #if the current record's price is less than the current recorded minimum 
            #for that particular stock
            if mins[record[0]] > int(record[2]):
                #update the minimum for that stock
                mins[record[0]] = int(record[2])
                
            #if the current record's price is greater than the current recorded maximum 
            #for that particular stock
            if maxs[record[0]] < int(record[2]):
                #update the minimum for that stock
                maxs[record[0]] = int(record[2])
            
        #If the stock name is not a key in the stocks dictionary, first create it as a key
        #in the stocks dictionary and set its value to an empty list
        #then, add the new record to that empty list
        else:
            stocks[record[0]] = []
            stocks[record[0]].append(record)
            
            #Create a key also in totals and set its value to the current record's price
            totals[record[0]] = int(record[2])
            #Create a key also in mins and set its value to the current record's price
            mins[record[0]] = int(record[2])
            #Create a key also in maxs and set its value to the current record's price
            maxs[record[0]] = int(record[2])
            
        #Read the next line of the file             
        fileLine = file.readline()

    #Indicate that the prepare function is finished 
    print('Done'.format(filename))
    
#Stock stats takes in specified stockname and returns min, mean and max price.
def stock_stats(stockName : str):
    print('Searching min, max, and mean price of stock : {}'.format(stockName))

    minprice = 0
    meanprice = 0
    maxprice = 0

    minprice = mins[stockName]
    maxprice = maxs[stockName]
    meanprice = round(int(totals[stockName])/len(stocks[stockName]),2)
    
    print("Min-price : {}, Mean-Price : {}, Max-Price : {} for stock : {}".format(minprice, meanprice, maxprice, stockName))

    # NOTE: please return these value with the following order: min, mean, max
    return minprice, meanprice, maxprice


