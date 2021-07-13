'''
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
'''
from typing import List

def Solve(nums:List[int])->int:
    ans = 0
    for i in nums: 
        count = 0
        while i>0: 
            i//=10
            count+=1 
        if count%2==0:
            ans+=1
    return ans 
if __name__=="__main__":
    nums = [555,901,482,1771]
    print(Solve(nums))