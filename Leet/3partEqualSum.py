'''
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
sum()
'''
from typing import List


def Solve(arr:List[int])->bool:
    total = sum(arr)
    if total%3 != 0:
        return False

    part_sum = total//3
    count = 0 
    res = 0
    for i in arr:
        res += i
        if res == part_sum:
            count+=1
            res = 0 
    return count >=3


if __name__=="__main__":
    arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    print(Solve(arr))