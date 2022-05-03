
#case-1 - array_split in 2D arrays
import numpy as np
arr=np.array([[2,3,1],[0,7,3],[9,4,5],[3,2,6],[4,7,5],[1,8,3]])
newarr=np.array_split(arr,2)
print(newarr)       #outputs:  [array([[2, 3, 1],
                                  #    [0, 7, 3],
                                   #    [9, 4, 5]]), array([[3, 2, 6],
                                  #    [4, 7, 5],
                                  #    [1, 8, 3]])]


#case-2 - adding axis to split along rows

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)   

# Outputs :
# [array([[ 1],
#        [ 4],
#        [ 7],
#        [10],
#        [13],
#        [16]]), array([[ 2],
#        [ 5],
#        [ 8],
#        [11],
#        [14],
#        [17]]), array([[ 3],
#        [ 6],
#        [ 9],
#        [12],
#        [15],
#        [18]])]
