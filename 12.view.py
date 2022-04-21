import numpy as np

arr=np.array([32,1,43,2])
x=arr.view()
arr[0]=9
print(arr)
print(x)

#view() does not own the data. Changes made to the original data will be refelected in the view() arr as well.
