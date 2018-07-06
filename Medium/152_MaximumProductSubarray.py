"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        #Time Limit Exceeded
        if len(nums) == 0:
            return 0
        res = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                tmp = 1
                for k in range(i, j + 1):
                    tmp *= nums[k]
                res = max(res, tmp)
        return res
        """
        if len(nums) == 0:
            return 0
        localmax = nums[0]
        localmin = nums[0]
        globalmax = nums[0]
        for i in range(1, len(nums)):
            tmp = localmax
            localmax = max(max(localmax * nums[i], nums[i]), localmin * nums[i])
            localmin = min(min(localmin * nums[i], nums[i]), tmp * nums[i])
            globalmax = max(globalmax, localmax)
        return globalmax
        