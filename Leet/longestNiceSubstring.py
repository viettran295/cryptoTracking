'''
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
set()
'''
from typing import Deque

def Solve(s:str)->str:
    cur_max = 0 
    res = ""
    for i in range(len(s)):
        upper = set()
        lower = set()
        if s[i].islower():
            lower.add(s[i])
        if s[i].isupper():
            upper.add(s[i].lower())
       
        for j in range(i+1,len(s)):
            if s[j].islower():
                lower.add(s[j])
            if s[j].isupper():
                upper.add(s[j].lower())
            if upper == lower:
                if j-i>cur_max:
                    cur_max = j-i
                    res = s[i:j+1]
    return res

if __name__=="__main__":
    s = "YazaAay"
    print(Solve(s))