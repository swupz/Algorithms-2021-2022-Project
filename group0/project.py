import utils

# Global data to store information
stocks = {}
sorted_data = []


def prepare(filename : str):
    print('Reading file {}'.format(filename))

    # Read from file and store into global data
    global your_variables_here
    your_variables_here = 'Somebody'

    global ds, data
    ds = open("../data/small_dataset.txt", "r")
    data = []
    rl = ds.readline()
    while rl is not "":
        frl = rl.split(',')
        frl[-1] = frl[-1][:0-2]
        data.append(frl)
        rl = ds.readline()

    # Read your file here and put the needed data into "your_variables_here".
    # you can also create complex data-structures here, if you need

    for set in data:
        if set[0] in stocks:
            sorted_data[stocks[set[0]]].append(set)
        else:
            stocks[set[0]] = len(stocks)
            sorted_data.append([set])

    print('Done'.format(filename))


def stock_stats(stockName : str):
    print('Searching min, max, and mean price of stock : {}'.format(stockName))
    # Search into global data for min, max and mean of the input stock

    '''
    if stock in your_variables_here:
        minprice, meanprice, maxprice = 0, 0, 0  # find the correct data
    else:
        minprice, meanprice, maxprice = 10, 20, 30  # find the correct data
    '''
    minprice = 0
    meanprice = 0
    maxprice = 0

    print(data[0][0])
    stocks = [stock for stock in data if stockName is stock[0]]
    print(stocks)

    print("Min-price : {}, Mean-Price : {}, Max-Price : {} for stock : {}".format(minprice, meanprice, maxprice, stockName))

    # NOTE: please return these value with the following order: min, mean, max
    return minprice, meanprice, maxprice
