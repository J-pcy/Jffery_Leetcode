"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        #O(n^2)
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)
        for i in range(len(nums)):
            tmpMax = -sys.maxsize
            tmpIndex = i
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    if dp[j] > tmpMax:
                        tmpMax = dp[j]
                        tmpIndex = j
            if tmpIndex < i:
                dp[i] = dp[tmpIndex] + 1
        return max(dp)
        """
        """
        #O(n^2)
        if len(nums) < 2:
            return len(nums)
        dp = [1] * len(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
        """
        #O(nlog(n))
        dp = []
        for i in range(len(nums)):
            start, end = 0, len(dp)
            while start < end:
                mid = start + (end - start) // 2
                if dp[mid] < nums[i]:
                    start = mid + 1
                else:
                    end = mid
            if end >= len(dp):
                dp.append(nums[i])
            else:
                dp[end] = nums[i]
        return len(dp)
        