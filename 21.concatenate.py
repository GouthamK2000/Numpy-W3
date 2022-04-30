
#case-1
import numpy as np

arr1=np.array([3,2,5,2,6])
arr2=np.array([7,0,3,5,3])
arr=np.concatenate((arr1,arr2)) #np.concatenate joins 2 arrays
print(arr)

#case-2

import numpy as np

arr1=np.array([[3,3,5],[2,5,6]])
arr2=np.array([[1,2,4],[0,2,9]])
arr=np.concatenate((arr1,arr2))
print(arr)

#arrays must be of the same dimensions, and the number of elements must be of the same size


#case-3

import numpy as np

arr1=np.array([[3,3,5],[2,5,6]])
arr2=np.array([[1,2,4],[0,2,9]])
arr=np.concatenate((arr1,arr2),axis=1)  # Here all the elements in first array (of both the arrays)are put into one array, similarly to the second.
print(arr)

