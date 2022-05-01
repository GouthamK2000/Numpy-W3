#case-1- vstack in 1D array

import numpy as np

arr1=np.array([1,4,2])
arr2=np.array([0,9,2])
arr=np.vstack((arr1,arr2))  #vstack stacks along columns
print(arr)                  #outputs-      [[1 4 2]
                            #              [0 9 2]]


#case -2- vstack in 2D arrays

import numpy as np

arr1=np.array([[4,3,2],[0,6,5]])
arr2=np.array([[5,8,4],[0,1,2]])
arr=np.vstack((arr1,arr2))
print(arr)                # outputs -         [[4 3 2]
                                  #           [0 6 5]
#                                             [5 8 4]
#                                             [0 1 2]]
 