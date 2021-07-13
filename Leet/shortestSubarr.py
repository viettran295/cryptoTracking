'''
Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], 
[2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
reverse()
min() max() Counter()
'''
from typing import Counter, List


def Solve(nums:List[int])->List[int]:
    rev = list(reversed(nums))
    mp = Counter(nums)
    pool = []
    for k,v in mp.items():
        if v == max(mp.values()):
            first = nums.index(k)
            second = rev.index(k)
            diff = len(nums) - second - 1
            pool.append(len(nums[first:diff+1]))
    return min(pool)
if __name__=="__main__":
    nums = [1,2,2,3,1]
    print(Solve(nums))