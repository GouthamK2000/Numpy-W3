
#case-1
import numpy as np

arr=np.array([3,5,2,4,2,0,])
newarr=np.array_split(arr,3)  #splits the array into the mentioned number of times
print(newarr)

#outputs :  [array([3, 5]), array([2, 4]), array([2, 0])]

#case-2 (number of elements need not be exactly divisible by the mentioned number)

import numpy as np

arr=np.array([0,3,5,2,5,1])
newarr=np.array_split(arr,4)
print(newarr)

#outputs :   [array([0, 3]), array([5, 2]), array([5]), array([1])]

#case 3 : Without printing the word array

import numpy as np

arr=np.array([45,24,0,76,2,1])
newarr=np.array_split(arr,3)
print(newarr[0])  
print(newarr[1])  
print(newarr[2])   

#outputs:
# [45 24]
# [ 0 76]
# [2 1]



#case 3 - Alternate method
import numpy as np

arr=np.array([45,24,0,76,2,1])
newarr=np.array_split(arr,3)
for i in range(2):
    print(newarr[i])      #outputs the same



