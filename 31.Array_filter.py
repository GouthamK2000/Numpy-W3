import numpy as np
arr=np.array([42,7,34,8,2,0])
x=[True,False,False,True,True,False]
newarr=arr[x]
print(newarr)  #outputs  [42  8  2]

#Here values that are mentioned true gets printed.

#the below mention thing happens generally.

import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)