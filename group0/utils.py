# Use this file to implement your own utils

##### HERE YOU CAN ADD YOUR UTILITY FUNCTIONS / OBJECT / CLASSES #####
import math

# Start mergesort is a step between calling mergesort for making it easier to call mergesort from another file.
def start_mergesort(unsorted_data):
    p = 0
    r = len(unsorted_data) - 1

    sorted_data = mergesort(unsorted_data, p, r)

    return sorted_data


# Mergesort divides the unsorted array, sorts it, and merges before returning the sorted array.
def mergesort(d, p, r):
    # Divide until only 2 values will be sorted.
    if (p < r):
        q = math.floor((p+r) / 2)
        mergesort(d, p, q)
        mergesort(d, q+1, r)
    # Sorts the divided data with bubblesort
    else:
        n = len(d)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if (d[j][2] > d[j+1][2]):       # Comparing value of the data
                    d[j], d[j+1] = d[j+1], d[j]

    return d
