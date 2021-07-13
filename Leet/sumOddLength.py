'''
Given an array of positive integers arr, 
calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
'''

from typing import List

# arr = [1,4,2,5,3]
def sumOdd(arr:List[int])->int:
    sumArr = 0 
    for i in range(len(arr)):
        for j in range(i,len(arr),2):
            sumArr += sum(arr[i:j+1])

