'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
'''
from typing import List
def Solve(nums1:List[int], nums2:List[int])->List[int]:
    both = set(nums1)&set(nums2)
    res = []
    for i in both:
        for _ in range(min(nums1.count(i),nums2.count(i))):
            res.append(i)
    return res

if __name__=="__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solve(nums1,nums2))    