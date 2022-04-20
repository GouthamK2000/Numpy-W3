import numpy as np

arr=np.arr([4,6,2,7,4])
x=arr.copy()
arr[0]=42
print(arr)   #prints the changed array
print(x)    #prints the original array