'''
Given a binary string s ​​​​​without leading zeros, 
return true​​​ if s contains at most one contiguous segment of ones. 
Otherwise, return false.
set(), s.strip()
'''
def Solve(s:str)->bool:
    check = False
    for i in s:
        if(i=='1'):
            if check:
                return False
        else:
            check = True
    return True
def SolveII(s:str)->bool:
    return set(s.strip('0'))==set('1')

if __name__=="__main__":
    s = '1001'
    print(SolveII(s))