'''
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
'''
from typing import List
def Solve(nums:List[int], k:int)->float:
    maxi = sum(nums[:k])
    current = maxi
    i = k
    start = 0 
    while i<len(nums):
        current = current+nums[i]-nums[start]
        maxi = max(current,maxi)
        i+=1
        start+=1
    return maxi/k

if __name__=="__main__":
    nums = [1,12,-5,-6,50,3]
    print(Solve(nums,4))