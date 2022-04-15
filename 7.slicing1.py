import numpy as np

arr=np.array([1,5,2,6])
print(arr[1:3])    # syntax=> [start:end],here value prints end-1

import numpy as np

arr=np.arr([3,4,2,4])
print(arr[1:2:2]) # syntax=> [start:end:skip], when not mentioned,  default value is zero

#negative indexing can also be used

import numpy as np

arr=np.array([2,3,5,1])
print(arr[::-1]) # here , the reverse of the mentioned arrays/string appear
