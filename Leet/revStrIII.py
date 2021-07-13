'''
Given a string s, reverse the order of characters 
in each word within a sentence 
while still preserving whitespace and initial word order.
s[i][::-1]: when reverse whole word
" ".join(s): space dan xen trong s 
'''
def Solve(s:str)->str:
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][::-1]
    return s
if __name__=="__main__":
    s = "Let's take LeetCode contest"
    print(Solve(s))