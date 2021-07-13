'''
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", 
with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
'''

from typing import ChainMap


def Solve(s:str)->str:
    stack = [] 
    check = set()
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            stack.append(i)
        else:
            tmp = stack.pop()
            if not stack: 
                check.add(tmp)
                check.add(i)
    ans = ""
    for i in range(len(s)):
        if i not in check:
            ans += s[i:i+1]
    return ans
if __name__=="__main__":
    s = "(()())(())"
    print(Solve(s))