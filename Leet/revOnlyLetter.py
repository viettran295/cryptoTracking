'''
Given a string s, 
return the "reversed" string where all characters that are not a letter stay in the same place, 
and all letters reverse their positions.
'''
def Solve(s:str)->str:
    s = list(s)
    i, j = 0, len(s)-1
    while i<j:
        if not s[i].isalpha():
            i+=1
        if not s[j].isalpha():
            j-=1
        if s[i].isalpha() and s[j].isalpha():
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
    return "".join(s)

if __name__=="__main__":
    s = "ab-cd"
    print(s[0])
    print(Solve(s))