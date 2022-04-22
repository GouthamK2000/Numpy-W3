import numpy as np
arr=np.array([4,2,5,2,5])
print(arr)
print(arr.shape)  #prints the number of eleements of  the specified array, prints 5.

import numpy as np
arr=np.array([[4,2,5,2,5],[5,2,4,2,5]])
print(arr)
print(arr.shape) #prints 2,5

import numpy as np
arr=np.array([4,2,5,2,5],ndmin=4)
print(arr)
print(arr.shape)  #prints [1,1,1,5],Total number of elements inside the array is going to be equivalent tondmin's value

#ndim and shape are not  the same. ndim says the dimension, shape tells us the size of the array.