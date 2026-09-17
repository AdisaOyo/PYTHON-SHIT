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

import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

# Aggregate functions = sumarize data and typically return a single value 

array = np.array([
                    [1,2,3,4,5],
                    [6,7,8,9,10]
                 ])

print(np.sum(array))

print(np.mean(array)) # mean
print(np.std(array)) # standard deviation
print(np.var(array)) # variance
print(np.argmin(array)) # will return index of minimmum value 

print(np.sum(array, axis=0)) # applying sum function to all columns 
print(np.sum(array, axis=1)) # applying sum function to all rows 


'''
FILTERING
'''

import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

# Filtering  = refers to the process of selecting elements from an array that match a given condition 

ages = np.array([
                  [21, 17, 19, 20, 16, 30, 18, 65],
                  [39, 22, 15, 99, 18, 19, 20, 21]
                ])

teenagers = ages[ages < 18] # boolian indexing. this will collaps the arra into one dimension. There are ways to preserve the dimensions but we will see that later 
print(teenagers)

## adults1 = ages[18 >= ages <= 65] # this will not work because the condition is not valid. we need to use the & operator to combine the two conditions
adults2 = ages[(ages >= 18) & (ages <65)] # this will work because the condition is valid. we need to use the & operator to combine the two conditions
seniors = ages[ages>=65]
print(adults2)
print(seniors)

evens = ages[ages % 2 == 0]
print(evens)

adults = np.where(ages >= 18, ages, 0)
print(adults)


'''
RANDOM NUMBERS
'''

import numpy as np # this is used to give numpy a nickname for convenience, so we don't have to type numpy every time we want to use it. Instead, we can just type np.

# 

rng = np.random.default_rng(seed=1) # this is used to create a random number generator object. The argument 1 is the seed for the random number generator. This means that the random numbers generated will be the same every time we run the code.

print(rng.integers(low = 1, high = 7))
print(rng.integers(low = 1, high = 101, size = 3))
print(rng.integers(low = 1, high = 101, size = (3, 2) )) #will give the random numbers in a 3 row, 2 column matrix

# if i dont set a seed Numpy will set one for me but if i do it will give me the same answer over and over again

np.random.seed(seed = 1) # this is used to set the seed for the random number generator. This means that the random numbers generated will be the same every time we run the code.
print(np.random.uniform(low = -1, high = 1, size = (3,3))) # uniform is for uniform disribution meaning every number has an equal chance of ocurring

rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array) # this is used to shuffle the elements of the array in place. This means that the original array will be modified and the elements will be rearranged randomly.
print(array)

rng = np.random.default_rng()
fruits = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
fruit = rng.choice(fruits, size = 3, replace = False) # this is used to randomly select elements from the array. The argument size = 3 means that we want to select 3 elements. The argument replace = False means that we do not want to select the same element more than once.
print(fruit)
