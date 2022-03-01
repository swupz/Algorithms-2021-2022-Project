# Use this file to implement your own utils

##### HERE YOU CAN ADD YOUR UTILITY FUNCTIONS / OBJECT / CLASSES #####
import math

def start_mergesort(unsorted_data):
    p = 0
    r = len(unsorted_data) - 1

    sorted_data = mergesort(unsorted_data, p , r)

    return sorted_data


def mergesort(d, p, r):
    if (p < r):
        q = math.floor((p+r) / 2)
        mergesort(d, p, q)
        mergesort(d, q+1, r)
    else:
        #sort (bubblesort?)
