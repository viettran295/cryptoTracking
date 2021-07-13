'''
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
from collections import deque
from typing import Deque


def isValid(s:str)->bool:
    valid = ['()','[]','{}']
    stack = deque([]) #deque: double end que
    for i in s:
        if not stack:
            stack.append(i)
            continue
        if(stack[-1]+i) in valid:
            stack.pop()
        else:
            stack.append(i)
    return len(stack)==0

if __name__=="__main__":
    s = '{}'
    print(isValid(s))