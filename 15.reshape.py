import numpy as np

arr=np.arr([3,1231,12,41,31,41,3,52,32,3,8,69])
newarr=arr.reshape([4,3,1])  #reshape(values) ,gives us an array of the required dimension.
print(newarr)

#another example
import numpy as np

arr=np.arr([3,1231,12,41,31,41,3,52,32,3,8,69])
newarr=arr.reshape([3,4,-1])  
print(newarr)

#by includeing -1, we need not specify the nth value. Out put is ame , irrespective of the position of the -1.
# -1 can only be specified once.
# if we have a multidimensional array, if we pass only -1, then we get 1D array, even if the initial array is 5D
