'''
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
from typing import List

def SolveII(nums:List[int], target:int)->List[int]:
    l = 0 
    r = len(nums)-1
    ans = []
    while l<r:
        sum = nums[l]+nums[r]
        if sum<target:
            l+=1
        elif sum>target:
            r-=1
        else:
            ans.append(l)
            ans.append(r)
            return ans
    return ans

def Solve(nums:List[int], target:int)->List[int]:
    mydict = dict()
    for i in range(len(nums)):
        mydict[nums[i]]=i

    for i in range(len(nums)):
        remain = target-nums[i]
        find = mydict.get(remain)
        if find and i!=find:
            return [i,find]

if __name__=="__main__":
    nums = [2,5,5,11]
    target = 10
    print(Solve(nums,target))
            