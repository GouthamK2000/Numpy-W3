import numpy as np

arr=np.array([42,1,413,13])
x=arr.copy()
y=arr.view()
print(x.base) #prints None
print(y.base)# print the array

#.base helps us find if the array owns its data or not.