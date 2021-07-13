'''
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number 
since it is the minimum in its row and the maximum in its column
'''
from typing import List
import numpy as np 

def Solve(matrix: List[List[int]])->List[int]:
    matrix = np.array(matrix)
    row = [] 
    ans = []
    row_len = matrix.shape[1]
    for i in range(row_len):
        row_max = np.max(matrix[:,i])
        row.append(row_max)
    for i in matrix:
        if np.min(i) in row:
            ans.append(np.min(i))
    return ans

    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(Solve(matrix))    