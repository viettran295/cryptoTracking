'''
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
sorted(nums)
'''
from typing import List
def Solve(nums:List[int])->int:
    nums = sorted(nums)
    return nums[-1]*nums[-2] - nums[0]*nums[1]

if __name__=="__main__":
    nums = [4,2,5,9,7,4,8]
    print(Solve(nums))