'''
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
'''
from typing import List
def Solve(s1:str, s2:str)->List[str]:
    l1 = s1.split()
    l2 = s2.split()
    dict1 = {}
    for i in l1:
        if i not in dict1:
            dict1[i]=0
        dict1[i]+=1
    for i in l2:
        if i not in dict1:
            dict1[i]=0
        dict1[i]+=1
    l = []
    for i in dict1:
        if dict1[i]==1:
            l.append(i)
    return l
if __name__=="__main__":
    s1 = "apple apple"
    s2 = "banana"
    print(Solve(s1,s2))