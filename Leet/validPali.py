'''
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
s[i:j][::-1]-> reverse print
'''

def Solve(s:str)->bool:
    i,j = 0, len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
        i+=1
        j-=1
    return True

if __name__=="__main__":
    s = 'abca'
    print(Solve(s))