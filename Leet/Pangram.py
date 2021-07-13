'''
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
set(), .add(...)
'''
def Solve(sentences:str)->bool:
    alphabet = set()
    nums = 0
    for char in sentences:
        if char not in alphabet:
            alphabet.add(char)
            nums+=1
        if nums == 26:
            return True
    return False

if __name__=="__main__":
    sentences = "thequickbrownfoxjumpsoverthelazydog"
    print(Solve(sentences))