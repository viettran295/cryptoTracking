'''
Two strings s and t are isomorphic if the characters in s can be replaced to get t.Two strings s and t are isomorphic 
if the characters in s can be replaced to get t.
Input: s = "paper", t = "title"
Output: true
dict()
'''
def Solve(s:str, t:str)->bool:
    if len(s)!=len(t):
        return False
    dict1 = {}
    for i in range(len(s)):
        if s[i] not in dict1:
            dict1[s[i]] = t[i]
        elif dict1[s[i]]!=t[i]:
            return False
    if len(set(s))!=len(set(t)):
        return False
    return True

if __name__=="__main__":
    s = "badc"
    t = "baba"
    print(Solve(s,t))