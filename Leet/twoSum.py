'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, 
we return [0, 1].
'''
from typing import List


def twoSum(nums:List[int], target:int)->List[int]:
    ans = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                ans.append(i)
                ans.append(j)
    return ans 

if __name__=="__main__":
    nums = [3,2,3]
    target = 6
    print(twoSum(nums, target))