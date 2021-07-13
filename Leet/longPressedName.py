'''
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Counter()
zip()
'''
from typing import Counter, List


def Solve(name:List[str],typed:List[str])->bool: 
    val = name[0]
    arr = []
    count = 1 
    for i in range(1,len(name)):
        if val == name[i]:
            count += 1
        else:
            arr.append([val,count])
            count = 1 
            val = name[i]
    arr.append([val,count])

    val = typed[0]
    arr2 = []
    for i in range(1,len(typed)):
        if val == typed[i]:
            count += 1
        else:
            arr2.append([val,count])
            count = 1 
            val = typed[i]
    arr2.append([val,count])

    if len(arr)==len(arr2):
        for i, j in zip(arr,arr2):
            if i[0]==j[0] and i[1]<=j[1]:
                continue
            else:
                return False
    else:
        return False
    return True

if __name__=="__main__":
    name = "alex"
    typed = "aaleex"
    print(Solve(name,typed))