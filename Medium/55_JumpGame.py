"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        #O(n^2)
        if len(nums) <= 1:
            return True
        res = [False] * len(nums)
        res[0] = True
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if res[j] and nums[j] >= i - j:
                    res[i] = True
                    break
        return res[-1]
        """
        """
        farthest = 0
        if len(nums) <= 1:
            return True
        for i in range(len(nums)):
            if farthest < i:
                return False
            else:
                farthest = max(farthest, i + nums[i])
                if farthest >= len(nums) - 1:
                    return True
        """
        farthest = 0
        if len(nums) <= 1:
            return True
        for i in range(len(nums)):
            if i <= farthest:
                farthest = max(farthest, i + nums[i])
            else:
                return False
        return farthest >= len(nums) - 1
        