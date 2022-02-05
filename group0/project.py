from . import utils

# Global data to store information
your_variables_here = ""

def prepare(filename : str):
    print('Reading file {}'.format(filename))

    # Read from file and store into global data
    global your_variables_here
    your_variables_here = 'Somebody'

    # Read your file here and put the needed data into "your_variables_here".
    # you can also create complex data-structures here, if you need

    print('Done'.format(filename))


def stock_stats(stock : str):
    print('Searching min, max, and mean price of stock : {}'.format(stock))
    # Search into global data for min, max and mean of the input stock
    if stock in your_variables_here:
        minprice, meanprice, maxprice = 0, 0, 0  # find the correct data
    else:
        minprice, meanprice, maxprice = 10, 20, 30  # find the correct data

    print("Min-price : {}, Mean-Price : {}, Max-Price : {} for stock : {}".format(minprice, meanprice, maxprice, stock))

    # NOTE: please return these value with the following order: min, mean, max
    return minprice, meanprice, maxprice
