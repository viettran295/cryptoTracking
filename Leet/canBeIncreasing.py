'''
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, 
it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.
'''
from typing import List


def Solve(nums:List[int])->bool:
    idx = -1
    count = 0 
    for i in range(len(nums)-1):
        if nums[i]>=nums[i+1]:
            idx += 1
            count += 1
    if count == 0:
        return True
    if count == 1:
        if idx == 0 or idx == len(nums)-2:
            return True
        if nums[idx-1]<nums[idx+1] or (idx+2<len(nums) and nums[idx]<nums[idx+2]):
            return True
    return False

if __name__=="__main__":
    nums = [1,2,10,5,7]
    print(Solve(nums))