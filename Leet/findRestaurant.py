'''
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
'''
from typing import List
import sys

def Solve(list1: List[str], list2: List[str]) -> List[str]:
    common = {}
    min_sum = float('inf')
    ans = [] 
    for idx, i in enumerate(list1):
        common[i] = idx
    for idx, i in enumerate(list2):
        if i in common:
            if idx+common[i] < min_sum:
                ans = [i]
                min_sum = idx + common[i]
            elif idx + common[i] == min_sum:
                ans.append(i)
    return ans
if __name__ == "__main__":
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    print(Solve(list1,list2))