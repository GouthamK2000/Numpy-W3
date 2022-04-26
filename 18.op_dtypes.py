import numpy as np

arr=np.array([5,3,2,45])
for i in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(i)


#flags=['bufferd] and op_dtypes=['S'], should be used inside np.nditer ONLY!
#We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
#NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].

#So both flags=['buffered] and , op_dtypes=['S'], should simultaneously  be declared.