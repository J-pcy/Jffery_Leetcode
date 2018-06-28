"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        nums.sort()
        for i in xrange(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
        """
        """
        #SUM
        num_sum = 0
        total_sum = 0
        for i in xrange(len(nums)):
            num_sum += nums[i]
            total_sum += i
        return total_sum+len(nums)-num_sum
        """
        #XOR
        res = 0
        for i in xrange(len(nums)):
            res ^= nums[i]^(i+1)
        return res
        