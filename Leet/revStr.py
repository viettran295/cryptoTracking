'''
Given a string s and an integer k, reverse the first k characters 
for every 2k characters counting from the start of the string.
reversed()
'''
def Solve(s:str, k:int)->str:
    s = list(s)
    for i in range(0,len(s),2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)

if __name__=="__main__":
    s = "abcdefg"
    print(Solve(s,2))