"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        res = []
        fproduct = [1]
        bproduct = [1] * len(nums)
        for i in range(1, len(nums)):
            fproduct.append(nums[i - 1] * fproduct[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            bproduct[i] = bproduct[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            res.append(fproduct[i] * bproduct[i])
        return res
        """
        res = [1]
        bproduct = 1
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * res[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            bproduct *= nums[i + 1]
            res[i] = res[i] * bproduct
        return res
        