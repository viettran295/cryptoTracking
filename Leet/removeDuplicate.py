'''
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent 
and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", 
of which only "aa" is possible, so the final string is "ca".
'''
def Solve(s:str)->str:
    stack = [s[0]]
    for i in range(1,len(s)):
        if stack and stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)

if __name__=="__main__":
    s = "abbaca"
    print(Solve(s))