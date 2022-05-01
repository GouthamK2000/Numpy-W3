#case-1- dstack in 1D array

import numpy as np

arr1=np.array([8,5,6])
arr2=np.array([8,0,3])
arr=np.dstack((arr1,arr2))   #dsatck stacks along depth, same as height
print(arr)

# outputs:
#              [[[8 8]
#                [5 0]
#              [6 3]]]


#case-2- dstack in 2D arrays

import numpy as np

arr1=np.array([[9,8,2],[4,6,3]])
arr2=np.array([[7,4,3],[5,6,3]])
rr=np.dstack((arr1,arr2))
print(rr)


# Outputs: 

# [[[9 7]
#   [8 4]
#   [2 3]]

#  [[4 5]
#   [6 6]
#   [3 3]]]