"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return nums
        res = []
        used = [False] * len(nums)
        nums.sort()
        self.dfs(nums, used, [], res)
        return res
    
    def dfs(self, nums, used, tmp, res):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for i in range(len(nums)):
            if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                continue
            if not used[i]:
                used[i] = True
                tmp.append(nums[i])
                self.dfs(nums, used, tmp, res)
                tmp.pop()
                used[i] = False
        