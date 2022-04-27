import numpy as np

arr=np.array([[23,5,23,35],[5,24,2124,3]])
for i in np.nditer(arr[:,::2]):  
    print(i)

 #np.nditer as usual.Slicing is used to print elements from both the arrays, one lement in a row.
 