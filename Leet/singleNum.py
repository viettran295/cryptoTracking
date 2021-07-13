'''
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity 
and use only constant extra space.
'''
arr = [1,1,2,5,6,6]
d = {}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    print(k, ' ', v)