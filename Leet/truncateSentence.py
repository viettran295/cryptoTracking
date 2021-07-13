'''
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
strip()
'''
def Solve(s:str,k:int)->str:
    l = s.split()
    ans = ""
    for i in range(k):
        ans+=l[i] + " "
    return ans.strip()

if __name__=="__main__":
    s = "hello how are you Viet"
    print(Solve(s,4))