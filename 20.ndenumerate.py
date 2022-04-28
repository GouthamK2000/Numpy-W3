#case 1:

import numpy as np

arr=np.array([4,2,4,1,1])
for y,x in np.ndenumerate(arr):   #2 vriables are declared while using ndenumerate function.
    print(y,x)


#nd enumerate is used while we need to print all the elements, along with each array elements index.
#Works perfectly for single or multi dimensional array.

#case 2:

import numpy as np

arr=np.array([[3,22,4,2,5,2],[5,3,24,24,24,28]])
for y,x in np.ndenumerate(arr):
    print(y,x)

