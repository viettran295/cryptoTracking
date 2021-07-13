'''
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''
def Solve(n:int)->int:
    product = 1
    sum = 0
    while n>0:
        product *= n%10
        sum += n%10
        n//=10
    return product-sum
if __name__ == "__main__":
    n = 4421
    print(Solve(n))
    