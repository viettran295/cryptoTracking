'''
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
max()
'''
from typing import List


def Solve(nums:List[int])->int:
    max_nums = max(nums)
    for i in range(len(nums)):
        if nums[i] == max_nums:
            idx = i 
        elif nums[i]*2>max_nums:
            return -1
    return idx

if __name__=="__main__":
    nums = [3,6,1,0]
    print(Solve(nums))

