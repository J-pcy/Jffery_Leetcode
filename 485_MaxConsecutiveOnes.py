"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        res = 0
        idx = 0
        tmp = 0
        while idx < len(nums):
            if nums[idx] == 1:
                tmp += 1
            else:
                tmp = 0
            res = max(res, tmp)
            idx += 1
        return res
        """
        res, tmp = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
            else:
                tmp = 0
            res = max(res, tmp)
        return res
        