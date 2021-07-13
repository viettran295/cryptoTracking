'''
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
'''
from typing import List

def summRanges(nums:List[int])->List[str]:
    if not nums:
        return []
    tmp = ''
    ans = []
    for i in range(len(nums)-1):
        if not tmp:
            tmp += str(nums[i])
            if nums[i+1]-nums[i]!=1:
                ans.append(tmp)
                tmp = ''
        else:
            if nums[i+1]-nums[i]!=1:
                tmp += '->'+str(nums[i])
                ans.append(tmp)
                tmp = ''
    if tmp:
        tmp += '->'+str(nums[-1])
        ans.append(tmp)
    else:
        ans.append(str(nums[-1]))
    return ans

nums = [0,1,2,3,8,9]
print(summRanges(nums))