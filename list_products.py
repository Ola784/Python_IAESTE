import random
import time


def products(list_):
    new_array=[]
    iloczyn=1
    leng=len(list_)
    
    for j in range(leng):
        iloczyn*=list_[j]
   

    for j in range(leng):
        new_array.append(int(iloczyn//list_[j]))

    return new_array


def products_no_division(list_):
    leng=len(list_)
    new_array=[1]*leng
    
    for j in range(leng):
        iloczyn=1
        for i in range(leng):
            if(i!=j):
                new_array[j]*=list_[i]
    return new_array


"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Do products() however u see fit, but also try implementing products_no_division() as name says, without using division.

Try to keep your implementations optimal.
"""

assert products([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert products([3, 2, 1]) == [2, 3, 6]

start = time.time()
products([random.randint(1, 50) for _ in range(10000)])
print(time.time() - start)

# share with us the time of your best implementation
# TIME: 0.14200758934020996
