def f(arr):
    #probowalam dac cos jak infinity, ale infinity jest float 
    for i in range(1,100):
        for j in range(len(arr)):
           # print(arr[j])
            if(arr[j]==i and arr[j]>0):#jesli znajde w array liczbe, przerywam dalsze przeszukiwanie array
                #print(f"znalezione: {arr[j]}")
                break
            elif(j==len(arr)-1):#jesli ostatni i nie znaleziono -> zwroc
                #print(f"liczba: {i}")
                return i
     

"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

assert f([3, 4, -1, 1]) == 2
assert f([1, 2, 0]) == 3
assert f([-6, 2, -3, 0]) == 1
assert f([1, 1, 2, 2, 4]) == 3
assert f([-1, -1, 0, 0, 2, 4, 1, 3]) == 5
