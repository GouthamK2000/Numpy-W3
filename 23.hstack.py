#case -1 hstack in 1D array

import numpy as np
arr1=np.array([2,3,6])
arr2=np.array([7,0,2])
arr=np.hstack((arr1,arr2)) #hstack, helps us to stack elements along rows.
print(arr)   #outputs -  [2 3 6 7 0 2]

#case-2 hsatck in 2D arrays

import numpy as np
arr1=np.array([[8,0,1],[3,5,8]])
arr2=np.array([[8,0,3],[0,3,1]])
arr=np.array((arr1,arr2))
print(arr)   #outputs [[8 0 1 8 0 3]
                     #[3 5 8 0 3 1]]

