#case-1 - sorting 1D arrays, numbers

import numpy as np

arr=np.array([6,3,5,25,8])
print(np.sort(arr))            #sort function returns the array in sorted order

#case-2 -sorting  1D arrays, words

import numpy as np

arr=np.array(["Goutham","Aditi","Poorani"])  
print(np.sort(arr))               #sort function sorts in alphabetical order as well


#case -3 -sorting 1D arrays, boolean

import numpy as np

arr=np.array([True,False,True])
print(np.sort(arr))               # In booleans, sort function helps us to sort in False to True order.(False<True)


#case-4 - sorting array in 2D arrays

import numpy as np

arr=np.array([[0,9,1,8,2,7,4],[4,6,2,6,7,3,1]])
print(np.sort(arr))               #in 2D arrays, both the the individual arrays get sorted, indidually. Here size of both the arrays must be equal.