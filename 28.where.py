#case-1

import numpy as np
arr=np.array([4,7,3,1,0,7,4])
x=np.where(arr==7)  #returns us all the indexes  where  specified number is present.
print(x)


#case-2

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.where(arr%2==0)  #returns us the indexes where elements are even number of elements, elements if divisible by 2.
print(x)

#case-3

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
x=np.where(arr%2==1)  #returns all the elements that leave a remainder of 1 when didided by 1
print(x)

