'''
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 
2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''
from typing import List

def Solve(arr:List[int])->bool:
    mp = {}
    for i in arr:
        if i in mp.keys():
            mp[i]+=1
        else:
            mp[i]=0
    if len(set(mp.values()))==len(mp.values()):
        return True
    return False
if __name__=="__main__":
    arr = [1,2]
    print(Solve(arr))