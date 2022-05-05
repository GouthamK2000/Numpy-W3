# case-1- searching an element(inbulit binary  search)

import numpy as np
arr=np.array([7,3,6,3])
x=np.searchsorted(arr,7)   #performs binary search and gives the  address of the specified elemnt's first occurence. 
print(x)
#Since binary search, it is sorted.
#HEre indexing starts from 0.

# case-2 - side-'right'

import numpy as np
arr=np.array([0,1,2,3,4])
x=np.searchsorted(arr,4,side='right')  #if side='right' is mentioned, indexing starts from 1.
print(x)

#searchsorted is used  only on sorted arrays.