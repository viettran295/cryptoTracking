'''
Given an array of strings words representing an English Dictionary,
return the longest word in words that can be built one character at a time by other words in words.
'''
from typing import List

def Solve(words:List[str])->str:
    words.sort()
    check = set()
    res = ""
    for i in words:
        if len(i)==1 or i[0:len(i)-1] in check:
            if len(i)>len(res):
                res = i
            check.add(i)
    return res

if __name__=="__main__":
    words = ["a","banana","app","appl","ap","apply","apple"]
    print(Solve(words))