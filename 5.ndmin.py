import numpy as np

arr=np.arr([1,2,3,4],ndmin=5) #equating a number with ndmin actually helps us to creat an array of specified dimension, even without creating such an array.
print(arr.ndim)