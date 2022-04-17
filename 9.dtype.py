import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)   #dtype returns the datatype

# #i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


import numpy as np
arr = np.array([1, 2, 3, 4],dtype='S') #dtype can be used here to change the data types.
print(arr.dtype)#outputs |s1


import numpy as np
arr = np.array([1, 2, 3, 4],dtype='S4') #further, bytes size can also be added
print(arr.dtype) #outputs |s4

#other data types along with which byte size can be added => i, u, f, S and U


