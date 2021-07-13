'''
Return true if each integer in the inclusive 
range [left, right] is covered by at least one interval in ranges. 
Return false otherwise.
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
'''
from typing import List


def Solve(ranges:List[List[int]], left:int, right:int)->bool:
    dicts = {}
    for i in range(left,right+1):
        dicts[i] = False
    for i in dicts:
        for start, end in ranges:
            if start<=i<=end:
                dicts[i] = True
                break
        if dicts[i] == False:
            return False
    return True

if __name__=="__main__":
    ranges = [[1,2],[3,4],[5,6]]
    left = 2
    right = 5
    print(Solve(ranges,left,right))

