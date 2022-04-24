#case 1:

import numpy as np

arr=np.array([2,1,3])
for x in arr:
    print(x)  #prints elements of the array, one element in a line


#case 2:
import numpy as np

arr=np.array([[2,1,3],[4,2,1]])
for x in arr:
    print(x) # prints 3 elements in a row, prints 2 1D arrays

#case 3:

import numpy as np

arr=np.array([[2,1,3],[4,2,1]])
for x in arr:
    for y in arr:
        print(y)    #prints all the elements of the initial array, one in a row.


#case 4:

import numpy as np
arr=np.array([[[3,2,2],[3,5,2]],[[0,5,2],[3,1,4]]])
for x in arr:
    print(x)  #same as case 2.

#case 5

import numpy as np
arr=np.array([[[3,2,2],[3,5,2]],[[0,5,2],[3,1,4]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)  #same as case 3, prints all elements of an array in a single row



