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
