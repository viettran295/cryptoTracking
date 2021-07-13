'''
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at 
the ith position moves to indices[i] in the shuffled string.
'''
from typing import List

def restoreString(s:str, indices:List[int])->str:
    d = {}
    for i in range(len(s)):
        d[indices[i]] = s[i]
    sort_d = sorted(d.keys())
    ans = ''
    for i in sorted(d):
        ans+=d[i]
    return ans

if __name__ == "__main__":
    s = 'codeleet'
    indices = [4,5,6,7,0,1,2,3]
    print(restoreString(s,indices))