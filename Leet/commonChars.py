'''
return a list of all characters that show up in all strings 
within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
Input: ["bella","label","roller"]
Output: ["e","l","l"]
defaultdict(list): {key: [val1, val2, val3]}
'''
from collections import defaultdict
from typing import DefaultDict, List


def Solve(words:List[str])->list[str]:
    dicts = defaultdict(list) #1 key: [many values]
    for i in words:
        sub = set(i)
        for j in sub:
            dicts[j].append(i.count(j))
    ans = []
    for i,j in dicts.items(): #dicts.items()
        if len(j)==len(words): #sizeof values == sizeof words
            ans += i*min(j) #min val in list(values)
    return ans

if __name__=="__main__":
    words = ["bella","label","roller"]
    print(Solve(words))