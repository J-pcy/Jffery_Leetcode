"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        #Time Limit Exceeded: O(n^3)
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i: j + 1]) == k:
                    res += 1
        return res
        """
        """
        #Time Limit Exceeded: O(n^2)
        res = 0
        for i in range(len(nums)):
            tmp = nums[i]
            if tmp == k:
                res += 1
            for j in range(i + 1, len(nums)):
                tmp += nums[j]
                if tmp == k:
                    res += 1
        return res
        """
        sumDict = {0: 1}
        tmpSum = 0
        res = 0
        for num in nums:
            tmpSum += num
            res += sumDict.get(tmpSum - k, 0)
            sumDict[tmpSum] = sumDict.get(tmpSum, 0) + 1
        return res
        