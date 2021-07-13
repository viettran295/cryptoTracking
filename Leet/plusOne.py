'''
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''
from typing import List
def plusOne(digits:List[int])->List[int]:
    for i in range(len(digits),0,-1):
        digits[i-1]+=1
        if digits[i-1]<=9:
            return digits
        else:
            digits[i-1] = 0
            if i-1==0:
                digits.insert(0,1)
    return digits
if __name__=="__main__":
    digits = [1,2,9]
    print(plusOne(digits))

