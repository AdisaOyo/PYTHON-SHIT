'''
PERSONAL NUMPY NOTES (LIBRARY BASICALLY)
'''

import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

#print (np.__version__) # this will print the version of numpy that is currently installed on your system.

my_list = [1, 2, 3, 4] #default python list
my_list = my_list*2 #multiply default python list by 2 resulting in the list repeating itself by the number of the operand 

array = np.array(my_list)

print (my_list)
print (array)
print (array*2) #multiply numpy array by 2 resulting in the array being multiplied by the number of the operand
print (type(array)) #this will print the type of the array, which is a numpy.ndarray
# nd means non dimentional. so nd array is ... guy you are smart you should know


'''
MULTIDIMENTIONAL ARRAYS
'''
import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

array_0d = np.array('A') #zero dimensional array
array_1d = np.array(['A', 'B', 'C']) #one dimensional array
array_2d = np.array([['A', 'B', 'C'],
                     ['D','E','F'],
                     ['G','H','I']]) #two dimensional array
#2d array is basically a matrix
array_3d = np.array([
                    [['A','B','C'],
                     ['D','E','F'],
                     ['G','H','I']],

                    [['J','K','L'],
                     ['M','N','O'],
                     ['P','Q','R']],

                     [['S','T','U'],
                      ['V','W','X'],
                      ['Y','Z','_']],
                     ]) #three dimensional array. All the lsits in the array need a conssent number of elements in each to make them work
print(array_0d.ndim) #ndim = number of dimensions
print(array_1d.ndim) 
print(array_2d.ndim)
print(array_3d.ndim)

print(array_3d.shape) #shape = number of elements in each dimension. In this case, the shape is (3, 3, 3) because there are 3 elements in the first dimension, 3 elements in the second dimension, and 3 elements in the third dimension.
# accessing data in array
print(array_3d[0][0][0]) #chain indexing
print(array_3d[0,0,1]) #multi-dimensional indexing. This is the preferred way to access data in a multi-dimensional array because it is more efficient and easier to read.

word = array_3d[0,0,0] + array_3d[2,0,0] + array_3d[2,0,0]
print(word)

'''
SLICING         
'''

import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

array = np.array([
                  [1,2,3,4], 
                  [5,6,7,8], 
                  [9,10,11,12], 
                  [13,14,15,16]
                ])
## access array using subscrip operaor
# array[start:end:step]
'''
ROW SELECTION
'''
print("printing out an entery in an array")
print(array[0])
# print(array[-2]) negative indexing starts the count from the last entry in the array to the top 
print("printing out an entery in an array from the starting index to the ending index")
print(array[0:3]) #slicing the array from index 0 to index 3 (not including index 3)
print("step array printing")
print(array[0:4:2]) #slicing the array from index 0 to index 4 (not including index 4) with a step of 2
print(array[::]) # i can use this to print the whole array or step with the scope of the whole array without putting a start or an end 
# you can use negative indexing to access the array from the end to the start

'''
COLUMN SEELECTION 
'''
print(array[0,0]) # this will print the first element in the first row and first column
print(array[:,0]) # this will print the first column of the array
print(array[:, 0:3]) # this will print the first three columns of the array

# basically it goes array[row,column]

'''
ARITHMETIC
'''

import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

# Scaler arithmetic [linear algebra. single value to entire array]

array = np.array([1,2,3])
array2 = np.array([1.01,2.5,3.99])
radii = np.array([1,2,3])

print(array + 1)
print(array - 1)
print(array * 2)
print(array / 2)
print(pow(array,2))

# Vectorised math finctions [single dimension, 1D list]

print(np.sqrt(array))
print(np.round(array2))
print(np.floor(array2))
print(np.ceil(array2))
print(np.pi)

print(np.pi*pow(radii,2)) #area of a circle = pi * r^2

# Element-wise arithmetic

array3 = np.array([1,2,3])
array4 = np.array([4,5,6])

print(array3 + array4)

# Comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)


'''
BROADCASTING
'''

import numpy as np
from numpy.char import array # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

# Broadcasting is a powerful feature of NumPy that allows for arithmetic operations between arrays of different shapes. It automatically expands the smaller array to match the shape of the larger array, enabling element-wise operations without the need for explicit replication.

# Broadcasting allows Numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# The dimensions have the same size
# OR
# One of the dimensions has a size of 1.

array1 = np.array([
                    [1,2,3,4]
                  ])
array2 = np.array([
                    [1],
                    [2],
                    [3],
                    [4]
                  ])

array3 = np.array([
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]
                  ])
array4 = np.array([
                    [1],
                    [2],
                    [3],
                    [4]
                  ])

print(array1.shape)
print(array2.shape)

print(array1*array2)
print(array3*array4)

# multipication table

arrayi = np.array([1,2,3,4,5,6,7,8,9,10])
arrayii = np.array([
                    [1],
                    [2],
                    [3],
                    [4],
                    [5],
                    [6],
                    [7],
                    [8],
                    [9],
                    [10]
                   ])

print(arrayi.shape)
print(arrayii.shape)
print("")
print(arrayi*arrayii)


'''
AGGREGATE FUNCTIONS
'''

