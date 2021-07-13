'''
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, 
you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, 
the next greater number for it in the second array is 3.
For number 2 in the first array, 
there is no next greater number for it in the second array, so output -1.
'''

from typing import List, NamedTuple

def Solve(nums1: List[int], nums2: List[int])->List[int]:
    stack = [] 
    dict = {}
    for i in nums2:
        while stack and stack[-1]<i:
            dict[stack.pop()] = i
        stack.append(i)
    for i in range(len(nums1)):
        try:
            nums1[i] = dict[nums1[i]]
        except:
            nums1[i] = -1
    return nums1

if __name__=="__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(Solve(nums1,nums2))
    
        