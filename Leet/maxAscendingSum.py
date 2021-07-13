'''
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
'''
from typing import List

def Solve(nums:List[int])->int:
    res = nums[0]
    tmp = nums[0]
    for i in range(1,len(nums)):
        if nums[i-1]<nums[i]:
            tmp += nums[i]
            if tmp>res:
                res = tmp
        else:
            tmp = nums[i]
    return res

if __name__=="__main__":
    nums = [10,20,30,5,10,50]
    print(Solve(nums))