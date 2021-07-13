'''
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''
from typing import List

def Solve(n:int)->List[int]:
    res = []
    for i in range(n+1):
        count = 0
        tmp = i
        while tmp:
            count += tmp & 1
            tmp >>= 1
        res.append(count)
    return res

if __name__=="__main__":
    n = 15
    print(n[1])