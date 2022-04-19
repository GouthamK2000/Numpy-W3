import numpy as np
arr=np.array([3,4,6,2])
newarr=arr.astype(dtype="f")  #astype can also be used to convert from one datatype to another
print(newarr)
print(newarr.dtype)


#example 2

import numpy as np
arr=np.arr([4,1,2,8])
newarr=arr.astype(dtype=bool)
print(newarr.dtype) #this return false for zero and true for anyother value apart from zero