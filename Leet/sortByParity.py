'''
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], 
and [4,2,1,3] would also be accepted.
'''
from typing import List


def sortParity(nums:List[int])->List[int]:
    even = 0
    for i in range(len(nums)):
        if nums[i]%2==0:
            nums[even], nums[i] = nums[i], nums[even]
            even+=1
    return nums
'''
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], 
[2,7,4,5] would also have been accepted.
'''
def sortParityII(nums:List[int])->List[int]:
    i = 0 
    j = 1
    while i<len(nums) and j<len(nums):
        if nums[i]&1==0:
            i+=2
        elif nums[j]&1:
            j+=2
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i+=2
            j+=2
    return nums
def sortParityIIs(nums:List[int])->List[int]:
    odd = []
    even = []
    for i in nums:
        if i&1:
            odd.append(i)
        else:
            even.append(i)
    nums[1::2] = odd
    nums[::2] = even
    return nums

if __name__=="__main__":
    nums = [4,2,5,7]
    print(sortParityIIs(nums))