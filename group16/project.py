import group16.utils as u

# Global data to store information
stocks = {}
sorted_data = []

# Prepare takes the data and sorts it by stock into a dictionary.
def prepare(filename : str):
    print('Reading file {}'.format(filename))

    # Read from file and store into global data
    global your_variables_here
    your_variables_here = 'Somebody'

    global ds, data
    ds = open(filename, "r")
    data = []
    rl = ds.readline()

    # Every line of the dataset it put into an array.
    while rl is not "":
        frl = rl.split(',')
        frl[-1] = frl[-1][:0-2]
        data.append(frl)
        rl = ds.readline()

    # Everything in the array is put in a dictionary sorted by stock.
    for set in data:
        # If the stock has a designated space in the sorted array, add the data there.
        if set[0] in stocks:
            sorted_data[stocks[set[0]]].append(set)
        # If not, makes space for the new stock in the sorted array and
        # saves the new stock and index for the sorted array.
        else:
            stocks[set[0]] = len(stocks)
            sorted_data.append([set])

    print('Done'.format(filename))


# Stock stats takes in specified stockname and returns min, mean and max price.
# First it sorts the stock data by price, and then finds the min, mean and max.
def stock_stats(stockName : str):
    print('Searching min, max, and mean price of stock : {}'.format(stockName))

    minprice = 0
    meanprice = 0
    maxprice = 0

    # Get the global data extracted in the prepare function.
    unsorted_dataStock = sorted_data[stocks[stockName]]

    # Uses mergesort from utils.py
    sorted_dataStock = u.start_mergesort(unsorted_dataStock)

    # First and last values of the sorted array equals min and max price.
    minprice = int(sorted_dataStock[0][2])
    maxprice = int(sorted_dataStock[-1][2])

    # Sums all the prices and calculates the mean.
    summedPrice = 0
    for data in sorted_dataStock:
        summedPrice += int(data[2])

    meanprice = summedPrice / len(sorted_dataStock)


    print("Min-price : {}, Mean-Price : {}, Max-Price : {} for stock : {}".format(minprice, meanprice, maxprice, stockName))

    # NOTE: please return these value with the following order: min, mean, max
    return minprice, meanprice, maxprice
