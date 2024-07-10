"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation. 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
import math

nums = [1,2,3,4]

def productExceptSelf(nums):

    answer = []
    left = []
    prod1 = 1
    right = []
    prod2 = 1
    i=0
    j=len(nums)-1
    while i in range(0,len(nums)):
        prod1 *= nums[i]
        prod2 *= nums[j]
        left.append(prod1)
        right.append(prod2)
        i += 1
        j -= 1
    right = list(reversed(right))
    for i in range(0,len(nums)):
        if i==0:
            answer.append(right[i+1])
        elif i==len(nums)-1:
            answer.append(left[i-1])
        else:
            answer.append(left[i-1] * right[i+1])
    return answer

result = productExceptSelf(nums)

print (result)