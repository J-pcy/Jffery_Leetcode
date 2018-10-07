"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """
        #Time Limit Exceeded O(n^3)
        res = sys.maxsize
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i: j + 1]) >= s:
                    res = min(res, j - i + 1)
        return 0 if res == sys.maxsize else res
        """
        """
        #O(n)
        start = 0
        subsum = 0
        res = sys.maxsize
        for i in range(len(nums)):
            subsum += nums[i]
            while start <= i and subsum >= s:
                res = min(res, i - start + 1)
                subsum -= nums[start]
                start += 1
        return 0 if res == sys.maxsize else res
        """
        #O(nlog(n))
        res = sys.maxsize
        sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
        for i in range(len(nums) + 1):
            right = self.binarySearch(i, len(nums), sums[i] + s, sums)
            if right == len(nums) + 1:
                break
            res = min(res, right - i)
        return 0 if res == sys.maxsize else res
    
    def binarySearch(self, left, right, target, sums):
        while left <= right:
            mid = left + (right - left) // 2
            if sums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        