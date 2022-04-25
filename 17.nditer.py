from gettext import npgettext
import numpy as np

arr=np.array([[3,2,45],[45,2,4]])

for i in np.nditer(arr):
    print(i)              # print all the elements, one in a row, irresective of the array dimension.

#This is very helpful when we use array of higher dimensions.