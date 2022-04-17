print(-10//3)
import numpy as np

arr=np.array([1,5,2,3])
print(arr[0])  # gives 1 as value, array indexing starts with a zero


import numpy as np
arr=np.array([1,2,3,4],[1,2,3,7])
print(arr[0,2]+arr[-1,-1]) #negative indexing can also be done, which conts the array from the reverse side


import numpy as np
arr=np.array([[[1,2,3,4],[1,2,3,7]],[[5,2,7,0],[0,1,4,2]]])
print(arr[-1,-1,1])  #indexing can involve both negative and positive signs