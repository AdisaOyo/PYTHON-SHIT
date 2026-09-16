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



