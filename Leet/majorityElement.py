'''
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
Counter(nums).most_common()[0][0]
dict()
'''
from typing import Counter, List


def Solve(nums:List[int])->int:
    check = dict()
    for i in nums:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
    
    max_check = max(check.values())
    for i in check:
        if check[i] == max_check:
            return i
            
def SolveII(nums:List[int])->int:
    return Counter(nums).most_common()[0][0]

if __name__=="__main__":
    nums = [2,2,1,1,1,2,2]
    print(Counter(nums).keys())