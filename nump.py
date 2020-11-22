'''Numpy Tutorials
NumPy is a general-purpose array-processing package. 
It provides a high-performance multidimensional array 
object, and tools for working with these arrays. It is 
the fundamental package for scientific computing with Python

What is an array
An array is a data structure that stores values of same data type.
In Python, this is the main difference between arrays and lists. 
While python lists can contain values corresponding to different 
data types, arrays in python can only contain values corresponding 
to same data type'''

import numpy as np

my_lst=[1,2,3,4,5]
arr = np.array(my_lst)
print(arr)
print(type(arr))

## Multinested array
my_lst1=[1,2,3,4,5]
my_lst2=[2,3,4,5,6]
my_lst3=[9,7,6,8,9]

arr1 = np.array([my_lst1,my_lst2,my_lst3])
print(arr1)
'''[[1 2 3 4 5]
 [2 3 4 5 6]
 [9 7 6 8 9]]
 this is a one-dimensional array
'''
print(arr1.shape)

print(arr1.reshape(5,3))
'''[[1 2 3]
    [4 5 2]
    [3 4 5]
    [6 9 7]
    [6 8 9]]
'''

# indexing in numpy array


arr2 = np.array([[1,2,3,4,5],
                [4,5,6,7,8],
                [1,2,3,9,4],
                [4,5,6,1,6]])

print(arr2.shape)
print(arr2[0:2,0:2])
print(arr2[1:,3:])
print(arr2[2:,2:4])
print(arr2[2:3,1:4])

#for elements in arr2:
    #print(elements)

# inbuilt functions of array
arr3 = np.arange(0,10,step=2)  #helps to create one -dimensional array
print(arr3)




arr4 = np.linspace(1,10,500)
# this function is usefull when we wants lots of point between
# two values  => we want 500 points between 1 to 10 that are 
# equally space
print(arr4)

#copy function and brodcasting
arr5 = np.arange(0,20)
print(arr5)
arr5[5:] = 10
print(arr5)

#here we are assigning arr5 into arr6 means
#=> if we made any changes with arr6 it will also reflect 
# in arr5 => refrence type follows
arr6 = arr5
print(arr6)
arr6[3:] = 500
print(arr6)  # arrays are refrence type
print(arr5)
 

 #to avoid the above problem we use copy function
 # copy function cretae another memory cell for arr6
arr6 = arr5.copy()
print(arr5)
arr6[3:] = 1000
print(arr6)

# some conditions which are useful for exploratoty data-analysis

val = 2
print(arr5<val)
# it prints the boolean value true where condition satifies
#[ True  True False False False False False False False False False False
#False False False False False False False False]

print(arr5[arr5<500])
# it returns the exact value
#[0 1 2]

print(arr5*5)
print(arr5/5)
print(arr5+5)
print(arr5-5)


arr7 = np.arange(1,10).reshape(3,3)
print(arr7)

arr8 = np.ones(12,dtype=int).reshape(4,3)
#creates an array having value of elements = 1
print(arr8)

#random distribution  0 < ele < 1
arr9 = np.random.rand(3,3)
print(arr9)

arr10 = np.random.randint(0,100,12).reshape(3,4)
print(arr10)

arr11 = np.random.random_sample((1,5))
print(arr11)
#standard normal distribution  































