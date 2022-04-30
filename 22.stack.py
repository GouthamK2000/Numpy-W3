#case-1
import numpy as np

arr1=np.array([2,4,7,2,6])
arr2=np.array([5,4,3,5,2])
arr=np.stack((arr1,arr2),axis=1)  #stack is same as concatenate except for one thing.
print(arr)

#First element is combined in both the arrays...Similarly all the elements.



#case-2
import numpy as np

arr1=np.array([[3,4,2],[7,0,9]])
arr2=np.array([[4,6,2],[2,0,9]])
arr=np.stack((arr1,arr2),axis=1)   #Here, first array in both the arrays are joined.Similarly the second one.
print(arr)