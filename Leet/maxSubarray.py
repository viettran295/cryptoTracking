'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
from typing import List

def Solve(nums:List[int])->int:
    maxx = nums[0]
    cur = 0 
    for i in nums:
        if cur<0:
            cur = 0
        cur += i
        maxx = max(maxx,cur)
    return maxx

if __name__=="__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solve(nums))