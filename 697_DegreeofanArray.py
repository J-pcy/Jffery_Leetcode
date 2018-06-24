"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degree = 0
        res = len(nums)
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = [1, i, i]
            else:
                nums_dict[nums[i]][0] += 1
                nums_dict[nums[i]][2] = i
            degree = max(degree, nums_dict[nums[i]][0])
        for i in nums_dict:
            if nums_dict[i][0] == degree:
                res = min(res, nums_dict[i][2] - nums_dict[i][1] + 1)
        return res
        